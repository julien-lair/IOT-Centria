#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from umqtt.robust import MQTTClient
import time



# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
MQTT_ClientID = 'testmqttThib'
MQTT_Broker = '172.20.10.9'
MQTT_Topic_Status = 'Lego/Status'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter = 54, axle_track = 105)

#callback for listen to topics
def listen(topic,msg):
    uneFois = False
    if topic == MQTT_Topic_Status.encode():
        ev3.screen.print(str(msg.decode()))
        if(str(msg.decode()) == 'go'):
            if(uneFois == False):
                robot.turn(90)
                robot.drive(300, 0)
                time.sleep(1.5)
                robot.turn(-90)
                robot.drive(300, 0)
                time.sleep(2.5)
                robot.turn(-90)
                robot.drive(300, 0)
                time.sleep(1.5)
                robot.turn(90)
                
                robot.stop()
                client.publish(MQTT_Topic_Status, 'clear')
                uneFois = True
        else:
            robot.stop()
            uneFois = False




# Write your program here.
#ev3.speaker.beep()

ev3.speaker.beep()
client.connect()
client.set_callback(listen)
client.subscribe(MQTT_Topic_Status)


while True:
    client.check_msg()
    time.sleep(0.5)
