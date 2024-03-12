from flask import Flask, request
import os
from google.cloud import bigquery
import requests
from datetime import datetime

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../caa-assignment1-174340d34e37.json"
client = bigquery.Client(project="caa-assignment1")

weather_api_key = "0c3c6755519a484ccf2c0741bedc8ebd" #YOUR_API_KEY
weather_url = f'http://api.openweathermap.org/data/2.5/weather?appid={weather_api_key}'
kelvin_sub = 273.15

# For authentication

YOUR_HASH_PASSWD = "7d23152dbf2c72714cd5be64064f3d7ac437c54539c80893b8d911a237f931c8" # YOUR_HAS_PASSWD

app = Flask(__name__)

# get the column names of the db
# PROJECT_ID.DATASET_ID.weather-records
q = """
SELECT * FROM `caa-assignment1.Lab4_IoT_datasets.weather-records` LIMIT 10
"""
query_job = client.query(q)
df = query_job.to_dataframe()

@app.route('/send-to-bigquery', methods=['GET', 'POST'])
def send_to_bigquery():
    if request.method == 'POST':
        if request.get_json(force=True)["passwd"] != YOUR_HASH_PASSWD:
            raise Exception("Incorrect Password!")
        data = request.get_json(force=True)["values"]
        # get the outdoor temp values
        city = request.args['city']
        response = requests.get(weather_url+f'&q={city}')
        outdoor_temp = round(response.json()['main']['temp'] - kelvin_sub)
        data["outdoor_temp"] = outdoor_temp
        outdoor_humidity = round(response.json()['main']['humidity'])
        data["outdoor_humidity"] = outdoor_humidity
        outdoor_weather = response.json()['weather'][0]['description']
        data["outdoor_weather"] = outdoor_weather
        # extract the date and time
        t = datetime.utcnow().timestamp()
        # consider the timezone
        t = datetime.fromtimestamp(t + response.json()['timezone'])
        data["date"] = str(t.date())
        data["time"] = f"{t.hour}:{t.minute}:00"
        # building the query
        # PROJECT_ID.DATASET_ID.weather-records
        q = """INSERT INTO `caa-assignment1.Lab4_IoT_datasets.weather-records` 
        """
        names = """"""
        values = """"""
        for k, v in data.items():
            names += f"""{k},"""
            if df.dtypes[k] == float:
                values += f"""{v},"""
            else:
                # string values in the query should be in single qutation!
                values += f"""'{v}',"""
        # remove the last comma
        names = names[:-1]
        values = values[:-1]
        q = q + f""" ({names})""" + f""" VALUES({values})"""
        query_job = client.query(q)
        return {"status": "sucess", "data": data}
    return {"status": "failed"}
        

@app.route('/get_outdoor_weather', methods=['GET', 'POST'])
def get_outdoor_weather():
    if request.method == 'POST':
        if request.get_json(force=True)["passwd"] != YOUR_HASH_PASSWD:
            raise Exception("Incorrect Password!")
        # get the latest outdoor temp values from the db
        # PROJECT_ID.DATASET_ID.weather-records
        q = """
        select outdoor_temp, outdoor_humidity from `caa-assignment1.Lab4_IoT_datasets.weather-records`
        order by date desc, time desc limit 1
        """
        query_job = client.query(q)
        df = query_job.to_dataframe()
        return df.iloc[0].to_dict()
    return {}


@app.route('/get_curr_time', methods=['GET'])
def get_curr_time():
    if request.method == 'GET':
        # we need this to get the timezone!
        city = request.args['city']
        response = requests.get(weather_url+f'&q={city}')
        dt_vals = {}
        # extract the date and time
        t = datetime.utcnow().timestamp()
        # consider the timezone
        t = datetime.fromtimestamp(t + response.json()['timezone'])
        dt_vals["date"] = str(t.date())
        dt_vals["time"] = f"{t.hour}:{t.minute}:00"
        return dt_vals
    return {}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)



