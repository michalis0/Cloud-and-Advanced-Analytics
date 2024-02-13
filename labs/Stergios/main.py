from flask import Flask, render_template, request, send_file
import requests

global co2val
co2val = 0


def getco2val():
    #update this section to ensure that the co2 value is returned from your big querry dataset (exercice 3)
    global co2val
    return co2val
def saveco2val(val):
    #update this section to ensure that the co2 value is updated on your big querry dataset (exercice 3)
    global co2val
    co2val = val


def gettemp():
    #update this section to ensure that the temperature is returned from your big querry dataset (exercice 3)
    global temp
    return temp
def saveTempCelcius(val):
    #update this section to ensure that the temperature is updated on your big querry dataset (exercice 3)
    global temp
    temp = val


def getTVOC():
    #update this section to ensure that the TVOC is returned from your big querry dataset (exercice 3)
    global TVOC
    return TVOC
def saveTVOC(val):
    #update this section to ensure that the TVOC is updated on your big querry dataset (exercice 3)
    global TVOC
    TVOC = val


global temp
saveTempCelcius(requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m&timezone=Europe%2FBerlin&forecast_days=1").json()['current']['temperature_2m'])

#This part identifies the home page of the website
weatherApp = Flask(__name__)
@weatherApp.route("/")
def run():
    return render_template("index.html")

@weatherApp.route("/sendTVOCToServer", methods=["get", "post"])
def sendTvocToServer():
    pass #change this abstract method to a concrete method that saves the TVOC value to your big querry dataset (exercice 2)


#This part controls the setter for the co2 value
@weatherApp.route("/sendECO2ToServer", methods=["get", "post"])
def sendDataToServer():
    if request.args.get("co2") != None:
        co2 = request.args.get("co2")
    else:
        try:
            co2 = request.json['co2']
        except:
            co2 = None
    if co2 == None:
        return """{"status": "error", "message": "no co2 value provided"}"""
    saveco2val(co2)
    return """{
        "status": "success",
        "data": %s
        }""" % (getco2val())


#This part controls the getter for the weather data
@weatherApp.route("/getWeatherData", methods=["get"])
def saveTVOC():
    saveTempCelcius(requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m&timezone=Europe%2FBerlin&forecast_days=1").json()['current']['temperature_2m'])
    return """{
        "status": "success", 
        "co2": %s, 
        "temperature": %d
        }""" % (getco2val(), gettemp())



@weatherApp.route("/downloadOutdoors", methods=["get"])
def downloadOutdoors():
    return send_file("static/assets/outdoors.m5f", as_attachment=True)
@weatherApp.route("/downloadIndoors", methods=["get"])
def downloadIndoors():
    return send_file("static/assets/indoors.m5f", as_attachment=True)

if __name__ == "__main__":
    weatherApp.run(host='0.0.0.0', port=80)