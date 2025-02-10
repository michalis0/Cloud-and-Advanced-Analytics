from flask import Flask, request
import os
from google.cloud import bigquery
import requests
from datetime import datetime

# You only need to uncomment the line below if you want to run your flask app locally.
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path-to-service-account-key-json"
client = bigquery.Client(project="test-caa-labs")


# For authentication

YOUR_HASH_PASSWD = "7d23152dbf2c72714cd5be64064f3d7ac437c54539c80893b8d911a237f931c8" # YOUR_HAS_PASSWD

app = Flask(__name__)

# get the column names of the db
# PROJECT_ID.DATASET_ID.weather-records
q = """
SELECT * FROM `test-caa-labs.lab4_dataset.weather-records` LIMIT 10
"""
query_job = client.query(q)
df = query_job.to_dataframe()

@app.route('/send-to-bigquery', methods=['GET', 'POST'])
def send_to_bigquery():
    if request.method == 'POST':
        if request.get_json(force=True)["passwd"] != YOUR_HASH_PASSWD:
            raise Exception("Incorrect Password!")
        data = request.get_json(force=True)["values"]
        # For exercise 2: Call the openweatherapi and add the resulting 
        # values to the `data` dictionary
        # data["outdoor_temp"] = ...
        # data["outdoor_humidity"] = ...
        # data["weather"] = ...
        # building the query
        q = """INSERT INTO `test-caa-labs.lab4_dataset.weather-records` 
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
        

# For exercise 3: Complete the following endpoint.
# @app.route('/get_outdoor_weather', methods=['GET', 'POST'])
# def get_outdoor_weather():
#     if request.method == 'POST':
#         if request.get_json(force=True)["passwd"] != YOUR_HASH_PASSWD:
#             raise Exception("Incorrect Password!")
#         # get the latest outdoor temp values from the db


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)



