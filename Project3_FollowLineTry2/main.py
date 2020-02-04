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


# Write your program here
left_motor = Motor(Port.D, Direction.CLOCKWISE, [40,24])
right_motor = Motor(Port.A, Direction.CLOCKWISE, [40,24])
robot = DriveBase(left_motor,right_motor,56,202)



filename = 'error.csv'
fobj = open(filename, 'w')

class MySensor(Ev3devSensor):  #Define Class 
    _ev3dev_driver_name="ev3-analog-01"
    def readvalue(self):
        self._mode('ANALOG')
        return self._value(0)

def control(right, left):
    direction = 1
    k_p = 0.05
    k_i = 0.5
    ldesired = 360
    rerror =  ldesired - right
    lerror = ldesired - left
    int_l = int_l+lerror
    int_r = int_r+rerror

    print('Left,'+str(lerror)+ ',Right,'+ str(rerror)+'\n')

    if (abs(lerror) > abs(rerror)):
        direction=-1
        
        anglechange = (k_p*abs(lerror) +k_i*int_l)
        anglechange = direction * anglechange
        #fobj.write('Left {}'.format(anglechange))
        fobj.write('Left,'+str(abs(lerror))+ ',Right,'+ str(abs(rerror))+'\n')
        return(anglechange)
    else:
        direction=1
        

        anglechange = (k_p*abs(rerror)+k_i*int_r)
        anglechange = direction * anglechange
        fobj.write('Left,'+str(abs(lerror))+ ',Right,'+ str(abs(rerror))+'\n')

        return(anglechange)

class controller(object):
    '''PID Controller Class for line follow robot'''
    def __init__(self, setpoint):
        self.setpoint = setpoint
        self.right = 0
        self.left = 0
        self.lerror = 0 
        self.rerror = 0
        self.int_l = 0
        self.int_r = 0
        self.k_p = 0.5
        self.k_i = 0.5

    def prop_control(self):
        self.lerror = self.setpoint - self.left
        self.rerror = self.setpoint - self.right

    def int_control(self):
        self.int_l += self.lerror
        self.int_r += self.rerror

    # def der_control(self):
    #     self.der_l_p = self.der_l
    #     self.der_r_p = self.der_r
    #     self.der_l = self.lerror - self.der_l_p
    #     self.der_r = self.rerror - self.der_r_p   

    def setangle(self):
        self.prop_control()
        self.int_control()
        anglechange = self.k_p * (abs(self.lerror)*-1 + abs(self.rerror)) 
        return anglechange

    # def lost(self):
    #     if self.lerror and self.rerror > 200:

# Write your program here
def main():
    #brick.sound.beep()
   
    sens = LegoPort(address ='ev3-ports:in3') # which port?? 1,2,3, or 4
    sens.mode = 'ev3-analog'
    

    utime.sleep(0.5)
    sensor_left=MySensor(Port.S1) # same port as above
    sensor_right=MySensor(Port.S3) # same port as above

    robot.drive(0,0)
    while True:
        lightLevel = sensor_left.readvalue()
        lightLevel2 = sensor_right.readvalue()
        ''' print('Left',lightLevel)
        print( 'Right', lightLevel2)'''
        controller.right = lightLevel2
        controller.left = lightLevel

        robot.drive(50,controller.setangle())
controller = controller(350)
main()
fobj.close()
