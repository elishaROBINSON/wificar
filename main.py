from wifi import wifi_connect
from umqtt.robust import MQTTClient
from config import *
from machine import Pin
import time 

up = Pin(4, Pin.OUT, value=1) #d0
down = Pin(5, Pin.OUT, value=1) #d1
left = Pin(6, Pin.OUT, value=1) #d2
right = Pin(7, Pin.OUT, value=1) #d3

wifi_connect(WIFI_SSID, WIFI_PASSWORD)
client = MQTTClient('esp8266',MQTT_HOST)

def exec(pin):
	pin.on()
	time.sleep(0.3)
	pin.off()

def drive(topic , msg):
	if msg == b"up":
		exec(up)
	elif msg == b"down":
		exec(down)
	elif msg == b"left":
		exec(left)
	elif msg ==b"right":
		exec(right)

client.set_callback(drive)
client.connect()
client.subscribe(MQTT_TOPIC)

try:
    while 1:
           client.wait_msg()
finally:
        client.disconnect()



