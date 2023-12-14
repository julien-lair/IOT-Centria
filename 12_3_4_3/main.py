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


# Create your objects here.
ev3 = EV3Brick()

while True:
    pressed_buttons = ev3.buttons.pressed()
    ev3.screen.clear()
    
    

    if Button.CENTER in pressed_buttons:
        ev3.speaker.play_notes(['A4/4'])
    elif Button.UP in pressed_buttons:
        ev3.speaker.play_notes(['B4/4'])
    elif Button.DOWN in pressed_buttons:
        ev3.speaker.play_notes(['B4/4'])
    elif Button.LEFT in pressed_buttons:
        ev3.speaker.play_notes(['C4/4'])
    elif Button.RIGHT in pressed_buttons:
        ev3.speaker.play_notes(['D4/4'])
    