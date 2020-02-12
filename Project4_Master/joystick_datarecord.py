#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from time import sleep 
import ubinascii, ujson, urequests, utime

xmotor = Motor(Port.A)
ymotor = Motor(Port.B)

with open('error.csv', 'a') as f:
    while True:
        f.write(str(xmotor.angle()) + ', '+ str(ymotor.angle())+'\n')
        wait(.01)
