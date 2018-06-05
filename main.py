from wifi import wifi_connect
from umqtt.robust import MQTTClient
from config import *
from machine import Pin
import time 

up = Pin(14, Pin.OUT, value=1) #d5
down = Pin(13, Pin.OUT, value=1) #d7
left = Pin(0, Pin.OUT, value=1) #d3
right = Pin(5, Pin.OUT, value=1) #d1
up.off()
down.off()
left.off()
right.off()

wifi_connect(WIFI_SSID, WIFI_PASSWORD)
client = MQTTClient('esp8266',MQTT_HOST)


def exec(pin):
	pin.on()
	time.sleep(0.1)
	pin.off()

def drive(topic , msg):
	print("message -> {} recieved on topic -> {} ".format(msg,topic))
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

print("completed connections waiting for signals")
try:
    while 1:
           client.wait_msg()
finally:
        client.disconnect()



