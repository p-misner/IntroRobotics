#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

from pybricks.ev3devio import Ev3devSensor 
import utime
import ev3dev2
from ev3dev2.port import LegoPort 
from math import *
import csv

filename = 'run.csv'
fobj = open(filename, 'w')
# Write your program here
left_motor = Motor(Port.D, Direction.CLOCKWISE, [40,24])
right_motor = Motor(Port.A, Direction.CLOCKWISE, [40,24])
robot = DriveBase(left_motor,right_motor,56,202)
list_left = []
list_right = []
class MySensor(Ev3devSensor):  #Define Class 
    _ev3dev_driver_name="ev3-analog-01"
    def readvalue(self):
        self._mode('ANALOG')
        return self._value(0)
def control(right, left):
    direction = 1
    k_p = .18
    ldesired = 360
    rerror =  ldesired - right
    lerror = ldesired - left
    list_left.append(left)
    list_right.append(right)
    if (lerror > rerror):
        direction=-1
        anglechange = abs(k_p*right)
        anglechange = direction * anglechange
        #fobj.write('Left {}'.format(anglechange))
        

        return(anglechange)
    else:
        direction=1
        anglechange = abs(k_p*right)
        anglechange = direction * anglechange
        return(anglechange)
    '''
    llight_desired = 200
    rlight_desired = 300
    rerror = right - rlight_desired
    lerror = left - llight_desired
    
        '''
    
# Write your program here
def main():
    brick.sound.beep()
    sens = LegoPort(address ='ev3-ports:in3') # which port?? 1,2,3, or 4
    sens.mode = 'ev3-analog'

    utime.sleep(0.5)
    sensor_left=MySensor(Port.S1) # same port as above
    sensor_right=MySensor(Port.S3) # same port as above

    robot.drive(0,0)
    while True:
        lightLevel = sensor_left.readvalue()
        lightLevel2 = sensor_right.readvalue() 

        print('Left',lightLevel)
        print( 'Right', lightLevel2)
        robot.drive(100,control(lightLevel2,lightLevel))

main()
fobj.close()
