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


motor1=Motor(Port.B, positive_direction=Direction.CLOCKWISE, gears=None)
motor2=Motor(Port.C, positive_direction=Direction.CLOCKWISE, gears=None)
# Write your program here.
robot = DriveBase(left_motor = motor1, right_motor = motor2, wheel_diameter=54, axle_track=105)


#MQTT setup
MQTT_ClientID = 'testmqtt'
MQTT_Broker = '172.20.10.9'
MQTT_Topic_Status = 'Lego/Status'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

#cqllbqck
def listen(topic,msg):
    if topic == MQTT_Topic_Status.encode():
        ev3.screen.print(str(msg.decode()))
        if(str(msg.decode()) == "clear"):
            robot.drive(200,0)
            client.publish(MQTT_Topic_Status, 'stop')


# Write your program here.


# Write your program here.
client.connect() 
client.set_callback(listen)
client.subscribe(MQTT_Topic_Status)
ev3.speaker.beep()
time.sleep(0.5) 
robot.drive(300,0)

UltraSensor=UltrasonicSensor(Port.S4)

stopSend = False
goSend = False
while True:
    client.check_msg()
    if(UltraSensor.distance() < 200):
        if(goSend == False):
            print("started")
            client.publish(MQTT_Topic_Status, 'go')
            robot.stop()
            time.sleep(3)
            goSend = True
            stopSend = False
    else:
        if(stopSend == False):
            print("stopped")
            client.publish(MQTT_Topic_Status, 'stop')
            stopSend = True
            goSend = False
        



