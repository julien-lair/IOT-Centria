#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

motor1=Motor(Port.B, positive_direction=Direction.CLOCKWISE, gears=None)
motor2=Motor(Port.C, positive_direction=Direction.CLOCKWISE, gears=None)
# Write your program here.
robot = DriveBase(left_motor = motor1, right_motor = motor2, wheel_diameter=54, axle_track=105)
# Create your objects here.
ev3 = EV3Brick()

CSensor=ColorSensor(Port.S3)
dernierDroite = True
while True:
    testdroite = False
    find = False
    ev3.screen.print(CSensor.color())
    if CSensor.color() == Color.BLACK:
        robot.drive(100,0)
    elif CSensor.color() == Color.RED:
        robot.stop()
        break
    elif CSensor.color() == Color.BLUE:
        robot.drive(20,0)
    else:
        robot.drive(0,0)
        if dernierDroite == True:
            ev3.screen.print("test droite")
            for i in range(0,5):
                if CSensor.color() != Color.BLACK and CSensor.color() != Color.BLUE:
                    robot.turn(5)
                else:
                    find = True
                    dernierDroite = True
            if find == False:
                robot.turn(-25)
                ev3.screen.print("test gauche")
                for i in range(0,5):
                    if CSensor.color() != Color.BLACK and CSensor.color() != Color.BLUE:
                        robot.turn(-5)
                    else:
                        find = True
                        dernierDroite = False
        else:
            ev3.screen.print("test gauche")
            for i in range(0,5):
                if CSensor.color() != Color.BLACK and CSensor.color() != Color.BLUE:
                    robot.turn(-5)
                else:
                    find = True
                    dernierDroite = False
            if find == False:
                robot.turn(25)
                ev3.screen.print("test droite")
                for i in range(0,5):
                    if CSensor.color() != Color.BLACK and CSensor.color() != Color.BLUE:
                        robot.turn(5)
                    else:
                        find = True
                        dernierDroite = True
            
       
        


    

# Write your program here.

