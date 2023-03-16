from m5mqtt import M5mqtt
import ntptime
import network 
import machine
import config
import utime

class Cloud:

    def __init__(self, jwt):
        sta_if = network.WLAN(network.STA_IF)

        self.__connect(sta_if)
        print("Connected to wifi")
        utime.sleep(5)
        self.__set_time()
        print("Time set")

        project_id = config.google_cloud_config['project_id']
        cloud_region = config.google_cloud_config['cloud_region']
        registry_id = config.google_cloud_config['registry_id']
        device_id = config.google_cloud_config['device_id']
        algorithm = config.jwt_config['algorithm']
        mqtt_bridge_hostname = config.google_cloud_config['mqtt_bridge_hostname']
        mqtt_bridge_port = config.google_cloud_config['mqtt_bridge_port']

        self.mqtt_topic = "/devices/{}/{}".format(device_id, "events")
        client_id = "projects/{}/locations/{}/registries/{}/devices/{}".format(
            project_id, cloud_region, registry_id, device_id
        )

        print("Creating MQTT Client")
        self.__client = M5mqtt(
            client_id,
            mqtt_bridge_hostname,
            port=mqtt_bridge_port,
            user="unused",
            password=jwt,
            keepalive=300,
            ssl=True,
            ssl_params={"cert": "/flash/roots.pem"}
        )
        print("Client created")

        self.__client.start()
        print("Client started")


    def __connect(self, sta_if):
        """Connect the divice to wifi it is not already the case """
        if not sta_if.isconnected():
            print('connecting to network...')
            sta_if.active(True)
            sta_if.connect(
                config.wifi_config['ssid'], config.wifi_config['password'])
        while not sta_if.isconnected():
            pass


    def __set_time(self):
        """ Set the time of the device """
        # ntptime.settime(timezone=1, server='ntp.ntsc.ac.cn')
        ntp = ntptime.client(host='ntp.ntsc.ac.cn', timezone=2)
        ntp.getTimestamp()
        tm = utime.localtime()
        tm = tm[0:3] + (0,) + tm[3:6] + (0,)
        machine.RTC().datetime(tm)
        print('current time: {}'.format(utime.localtime()))


    def publish(self, payload):
        """ Publish the paylaod to the topic """
        print("publish payload : " + str(payload) + " to topic : " + str(self.mqtt_topic))
        self.__client.publish(self.mqtt_topic, payload, qos=1)
        
    def receive(self):
        """ TODO """
        pass
