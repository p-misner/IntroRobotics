#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

from pybricks.ev3devio import Ev3devSensor 
import utime, uio
import ev3dev2
from ev3dev2.port import LegoPort 
#import matplotlib
#brick.sound.beep()

time = StopWatch()
time.reset()

btn = TouchSensor(Port.S2)

filename = 'test.txt'
fin = open(filename, 'w')
fin.close()

timepressed = []


begin = False
starttime = 0
endtime = 0
while True:
    if btn.pressed() and begin ==False:
        starttime = time.time()
        begin = True
    if not btn.pressed() and begin==True:
        endtime = time.time()
        begin = False
        timepassed = endtime - starttime
        timepressed.append(timepassed/1000)
    if len(timepressed) == 15:
        #fin.write(timepressed)
        brick.sound.beep()
        print('DOT',timepressed)
        timepressed = []
    elif len(timepressed) == 30:
        print('DASH',timepressed)
        #fin.write(timepressed)
        break
    



