from m5stack import *
from m5stack_ui import *
from uiflow import *
import time
import unit
import urequests
import hashlib
import binascii


screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xd5d5d5)
env3_0 = unit.get(unit.ENV3, unit.PORTA)
temp_flag = 300

passwd = "CAA24_Ahmad"
h = hashlib.sha256(passwd)
passwd_hash = binascii.hexlify(h.digest())


Temp = M5Label('Temp:', x=19, y=142, color=0x000, font=FONT_MONT_22, parent=None)
Humidity = M5Label('Humidity:', x=19, y=183, color=0x000, font=FONT_MONT_22, parent=None)
label0 = M5Label('T', x=163, y=142, color=0x000, font=FONT_MONT_22, parent=None)
label1 = M5Label('H', x=158, y=183, color=0x000, font=FONT_MONT_22, parent=None)
label2 = M5Label('date', x=110, y=14, color=0x000, font=FONT_MONT_22, parent=None)
label3 = M5Label('T', x=245, y=142, color=0x000, font=FONT_MONT_22, parent=None)
label4 = M5Label('H', x=241, y=183, color=0x000, font=FONT_MONT_22, parent=None)
label5 = M5Label('time', x=110, y=66, color=0x000, font=FONT_MONT_30, parent=None)
label6 = M5Label('In', x=158, y=103, color=0x000, font=FONT_MONT_18, parent=None)
label7 = M5Label('Out', x=234, y=103, color=0x000, font=FONT_MONT_18, parent=None)


while True:
  dt_response = urequests.get("https://weather-api-2-c45baz7vfq-lz.a.run.app/get_curr_time?city=Lausanne")
  dt_response = dt_response.json()
  label2.set_text(str(dt_response["date"]))
  label5.set_text(str(":".join(dt_response["time"].split(":")[:-1])))
  label0.set_text(str(round(env3_0.temperature)))
  label0.set_text_color(0x000000)
  label1.set_text(str(round(env3_0.humidity))+" %")
  label1.set_text_color(0x000000)
  # get temp every 5 minutes
  if temp_flag == 300:
    data = {
        "passwd": passwd_hash,
        "values": {
            "indoor_temp": round(env3_0.temperature),
            "indoor_humidity": round(env3_0.humidity)
        }
    }
    urequests.post("https://weather-api-2-c45baz7vfq-lz.a.run.app/send-to-bigquery?city=Lausanne", json=data)
    data = {
        "passwd": passwd_hash
    }
    response = urequests.post("https://weather-api-2-c45baz7vfq-lz.a.run.app/get_outdoor_weather", json=data)
    label3.set_text(str(round(response.json()['outdoor_temp'])))
    label4.set_text(str(round(response.json()['outdoor_humidity']))+" %")
    temp_flag = 0
  temp_flag += 1
  wait(1)
  wait_ms(2)
  
  
  
  
  
  
  
  