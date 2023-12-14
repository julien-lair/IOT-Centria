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



#MQTT setup
MQTT_ClientID = 'testmqtt'
MQTT_Broker = '172.20.10.9'
MQTT_Topic_Status = 'Lego/Status'

MQTT_Topic_Status_2 = 'Distance/Status'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

#cqllbqck
def listen(topic,msg):
    if topic == MQTT_Topic_Status_2.encode():
        ev3.screen.print("distance {} mm".format(str(msg.decode())))



# Write your program here.


# Write your program here.
client.connect() 
client.set_callback(listen)
client.subscribe(MQTT_Topic_Status_2)


ev3.speaker.beep()
time.sleep(0.5) 

dernierStop = False
haut = False
bas = False
gauche = False
droite = False
while True:
    client.check_msg()
    pressed_buttons = ev3.buttons.pressed()
    if Button.UP in pressed_buttons:
        if(haut == False):
            print("haut")
            client.publish(MQTT_Topic_Status, 'haut')
            dernierStop = False
            haut = True
            bas = False
            gauche = False
            droite = False
    elif Button.DOWN in pressed_buttons:
         if(bas == False):
            print("bas")
            client.publish(MQTT_Topic_Status, 'bas')
            dernierStop = False
            haut = False
            bas = True
            gauche = False
            droite = False
    elif Button.LEFT in pressed_buttons:
        if(gauche == False):
            print("gauche")
            client.publish(MQTT_Topic_Status, 'gauche')
            dernierStop = False
            haut = False
            bas = False
            gauche = True
            droite = False
    elif Button.RIGHT in pressed_buttons:
        if(droite == False):
            print("droite")
            client.publish(MQTT_Topic_Status, 'droite')
            dernierStop = False
            haut = False
            bas = False
            gauche = False
            droite = True
    else:
        if(dernierStop == False):
            print("rien")
            client.publish(MQTT_Topic_Status, 'rien')
            dernierStop = True
            haut = False
            bas = False
            gauche = False
            droite = False



