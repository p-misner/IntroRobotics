#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.iodevices import UARTDevice
brick.sound.beep()

ymotor = Motor(Port.B, Direction.CLOCKWISE)
xmotor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
direction = 1

uart = UARTDevice(Port.S3, 9600, timeout=10000)

wait(500)

uart.write('a')
print("Done")

curr = ""
previous = 'q'
uart.write('q')
while True:
    xangle = xmotor.angle()
    yangle = ymotor.angle()
    print(str(xangle) + " " + str(yangle))
    if yangle > 20 and xangle > 20:
        curr = 'x'
    elif yangle > 20 and (xangle < 20 and xangle > -20):
        curr = 'y'
    elif yangle > 20 and (xangle < -20):
        curr = 'z'
    elif (yangle < 20 and yangle > -20) and xangle < -20:
        curr = 's'
    elif (yangle < -20) and xangle < -20:
        curr = 't'
    elif (yangle < -20) and (xangle < 20 and xangle > -20):
        curr = 'u'
    elif (yangle < -20) and (xangle > 20):
        curr = 'v'
    elif (yangle > -20 and yangle < 20) and xangle > 32:
        curr = 'w'
    else:
        curr = 'q'
    if previous != curr:
        uart.write(curr)
        previous = curr
    wait(.1)
