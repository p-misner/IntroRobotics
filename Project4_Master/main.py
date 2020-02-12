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
hapticmotor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
direction = 1
print('????')
uart = UARTDevice(Port.S4, 9600, timeout=10000)

wait(500)

uart.write('a')

curr = ""
previous = 'q'
uart.write('q')
while True:
    xangle = xmotor.angle()
    yangle = ymotor.angle()
    #print(str(xangle) + " " + str(yangle))
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
    elif (yangle > -20 and yangle < 20) and xangle > 15:
        curr = 'w'
    else:
        curr = 'q'
    if previous != curr:
        uart.write(curr)
        previous = curr
    if uart.waiting() != 0:
        holder = uart.read(1)
        '''if  holder == b'b': 
            print('b')
            hapticmotor.run(40)
        else:
            print('empty')
            hapticmotor.run(0)'''
        
    wait(.1)
    