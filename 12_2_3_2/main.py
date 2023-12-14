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


# Create your objects here.
ev3 = EV3Brick()

motor1=Motor(Port.B, positive_direction=Direction.CLOCKWISE, gears=None)
motor2=Motor(Port.C, positive_direction=Direction.CLOCKWISE, gears=None)
# Write your program here.
robot = DriveBase(left_motor = motor1, right_motor = motor2, wheel_diameter=54, axle_track=105)


robot.drive(250,80)
time.sleep(3.4)
robot.drive(250,-80)
time.sleep(3.4)