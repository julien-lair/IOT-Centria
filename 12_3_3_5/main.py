#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

motor1=Motor(Port.B, positive_direction=Direction.CLOCKWISE, gears=None)
motor2=Motor(Port.C, positive_direction=Direction.CLOCKWISE, gears=None)
# Write your program here.
robot = DriveBase(left_motor = motor1, right_motor = motor2, wheel_diameter=54, axle_track=105)
# Create your objects here.
ev3 = EV3Brick()

CSensor=ColorSensor(Port.S3)
TSensor=TouchSensor(Port.S1)
red = 0
black = 0
blue = 0
blackTrouve = False
redTrouve = False
blueTrouve = False
button = False
tabColor = []
while True and button == False: 
    ev3.screen.print("R: " + str(red) + "N: " + str(black) + "B: " + str(blue))
    if TSensor.pressed() == True:
        button = True
        robot.drive(0,0)
        
    
        
    else:
        robot.drive(100,0)
        if CSensor.color() == Color.BLACK and blackTrouve == False:
            print("noir")
            black += 1
            blackTrouve = True
            redTrouve = False
            blueTrouve = False
            tabColor.append("black")
        if CSensor.color() == Color.RED and redTrouve == False:
            print("rouge")
            red += 1
            redTrouve = True
            blackTrouve = False
            blueTrouve = False
            tabColor.append("red")
        if CSensor.color() == Color.BLUE and blueTrouve == False:
            print("bleu")
            blue += 1
            blueTrouve = True
            redTrouve = False
            blackTrouve = False
            tabColor.append("blue")
        if CSensor.color() == Color.WHITE:
            blackTrouve = False
            redTrouve = False
            blueTrouve = False
        
if button == True:
        #parcour le tableau tabColor
        for color in tabColor:
            if color == 'red':
                ev3.speaker.play_notes(['A4/4'])
            elif color == 'black':
                ev3.speaker.play_notes(['C4/4'])
            elif color == 'blue':
                ev3.speaker.play_notes(['E4/4'])
            time.sleep(0.2)
        robot.drive(0,0)