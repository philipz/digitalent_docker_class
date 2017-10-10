#!/usr/bin/env python3
import paho.mqtt.publish as publish
from subprocess import check_output
from re import findall

def get_temp():
    temp = check_output(["cat","/sys/class/thermal/thermal_zone0/temp"])
    return(str(float(temp)/1000))

def publish_message(topic, message):
    print("Publishing to MQTT topic: " + topic)
    print("Message: " + message)

    publish.single(topic, message, hostname="192.168.2.11")

temp = get_temp()
publish_message("Home/RPI3/Temp", temp)
