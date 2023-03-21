from m5stack import *
from m5ui import *
from uiflow import *
from m5mqtt import M5mqtt


project_id = "YOUR PROJECT ID"
cloud_region = "YOUR CLOUD REGION"
registry_id = "YOUR REGISTRY ID"
device_id = "YOUR DEVICE ID"
jwt = "YOUR_JWT"
wifi_ssid="YOUR_WIFI_SSID"
wifi_password= "YOUR_WIFI_PASSWORD"

#I did not verify whether the "format" function works in micropython, if it does not
#please manually enter the values in the strings

client_id = "projects/{}/locations/{}/registries/{}/devices/{}".format(
    project_id, cloud_region, registry_id, device_id
)

mqtt_topic = "/devices/{}/events".format(device_id)

mqtt_bridge_hostname='mqtt.googleapis.com'
mqtt_bridge_port = 8883




setScreenColor(0x222222)
label0 = M5TextBox(51, 101, "label0", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label0.setText('Hello!')


try:
  import network 
  sta_if = network.WLAN(network.STA_IF)
  if not sta_if.isconnected():
              label0.setText('Connecting to network...')
              wait(3)
              sta_if.active(True)
              sta_if.connect(
                  wifi_ssid, wifi_pwd)
  while not sta_if.isconnected():
    pass
  label0.setText('Connected')
  wait(3)
except:
  label0.setText('Error in connecting to Wifi')
  wait(3)






try:
  client = M5mqtt(
              client_id,
              mqtt_bridge_hostname,
              port=mqtt_bridge_port,
              user="unused",
              password=jwt,
              keepalive=300,
              ssl=True,
              ssl_params={"cert": "/flash/roots.pem"}
          )
          
  client.start()
  
  for i in range(10, 15):
    payload = "payload number {}".format(i)
    client.publish(mqtt_topic, payload, qos=1)
    label0.setText("payload number {} published".format(i))
    wait_ms(1000)
  label0.setText('Published')
  wait(3)
  
except:
  label0.setText('Error in connecting to mqtt')
  wait(3)
        
        
        
        
        
        
        
        
        
        
        
        