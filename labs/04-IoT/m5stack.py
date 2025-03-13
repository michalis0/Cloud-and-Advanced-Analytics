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

passwd = "<YOUR_PASSWORD>"
h = hashlib.sha256(passwd)
passwd_hash = binascii.hexlify(h.digest())


Temp = M5Label('Temp:', x=19, y=142, color=0x000, font=FONT_MONT_22, parent=None)
Humidity = M5Label('Humidity:', x=19, y=183, color=0x000, font=FONT_MONT_22, parent=None)
label0 = M5Label('T', x=163, y=142, color=0x000, font=FONT_MONT_22, parent=None)
label1 = M5Label('H', x=158, y=183, color=0x000, font=FONT_MONT_22, parent=None)
label6 = M5Label('In', x=158, y=103, color=0x000, font=FONT_MONT_18, parent=None)
label7 = M5Label('Out', x=234, y=103, color=0x000, font=FONT_MONT_18, parent=None)


while True:
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
    urequests.post("<URL_FROM_CLOUDRUN>/send-to-bigquery", json=data)
    temp_flag = 0
  temp_flag += 1 # counter for the 300 seconds wait to update the temperature info.
  wait(1)
  wait_ms(2)