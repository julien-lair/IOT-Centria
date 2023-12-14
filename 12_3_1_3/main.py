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


# Write your program here.

TSensor=TouchSensor(Port.S1)

#5 seconds
seconde = 5
touch = 0
while(seconde > 0):
    if TSensor.pressed():
        touch = touch + 1
        ev3.screen.print(touch)
    seconde -= 0.5
    time.sleep(0.5)

for i in range(0, touch):
    ev3.speaker.beep()
    time.sleep(0.5)


