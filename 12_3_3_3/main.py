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

while True:
    if CSensor.color() == Color.RED:
        ev3.speaker.play_notes(['A4/4'])
    elif CSensor.color() == Color.BLUE:
        ev3.speaker.play_notes(['B4/4'])
    elif CSensor.color() == Color.GREEN:
        ev3.speaker.play_notes(['C4/4'])
    elif CSensor.color() == Color.YELLOW:
        ev3.speaker.play_notes(["D4/4"])

    

# Write your program here.

