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


class controller(object):
    '''PID Controller Class for line follow robot'''
    def __init__(self, setpoint_l, setpoint_r):
        self.setpoint_r = setpoint_r
        self.setpoint_l = setpoint_l
        self.right = 0
        self.left = 0
        self.lerror = 0 
        self.rerror = 0
        self.int_l = 0
        self.int_r = 0
        self.der_l = 0
        self.der_r = 0
        self.der_l_p = 0
        self.der_r_p = 0
        
        
        self.k_p = 0.6
        self.k_i = 0
        self.k_d = 0

    def prop_control(self):
        #self.left *= 1.25
        self.lerror = self.setpoint_l - self.left
        self.rerror = self.setpoint_r - self.right
        fobj.write('Left,'+str((self.lerror))+ ',Right,'+ str((self.rerror))+'\n')
    def int_control(self):
        self.int_l += self.lerror
        self.int_r += self.rerror
        fobj.write(',,,,Left Integ,'+str((self.int_l))+ ',Right Integ,'+ str((self.int_r))+'\n')
        

    def der_control(self):
        self.der_l_p = self.der_l
        self.der_r_p = self.der_r
        self.der_l = self.lerror - self.der_l_p
        self.der_r = self.rerror - self.der_r_p   
        fobj.write(',,,,,,,,Left Deriv,'+str(self.der_l)+ ',RightDeriv,'+str(self.der_r)+'\n')

    def setangle(self):
        self.prop_control()
        self.int_control()
        self.der_control()
        # proportional control (self.k_p * (abs(self.lerror)*-1 + abs(self.rerror))) +
        anglechange = (self.k_p * (abs(self.lerror)*-1+ abs(self.rerror)))
        fobj.write(',,,,,,,,,,,,Output,'+str((anglechange))+'\n')
        #anglechange += (self.k_d * (self.der_l+self.der_r))
        '''if self.lerror > self.rerror:
            anglechange += (self.k_i * ( self.int_l))
            anglechange += (self.k_d * (self.der_l))
        else: 
            anglechange += (self.k_i * ( self.int_r))
            anglechange += (self.k_d * (self.der_r))'''
        return anglechange

    # def lost(self):
    #     if self.lerror and self.rerror > 200:

# Write your program here
def main():
    #brick.sound.beep()
   
    sens = LegoPort(address ='ev3-ports:in1') # which port?? 1,2,3, or 4
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
        controller.right = lightLevel2
        controller.left = lightLevel

        robot.drive(50,controller.setangle())

controller = controller(400, 400)
main()
fobj.close()
