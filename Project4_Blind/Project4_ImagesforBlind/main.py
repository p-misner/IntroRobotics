#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
'''from pybricks.ev3devio import Ev3devSensor 
import utime
import ev3dev2
from ev3dev2.port import LegoPort '''

# Write your program here
brick.sound.beep()

filename = 'error.csv'
fobj = open(filename, 'w')

#stationary = Motor(Port.D, Direction.CLOCKWISE)
#rotating = Motor(Port.B, Direction.CLOCKWISE)

#right_motor = Motor(Port.C, Direction.CLOCKWISE)
#left_motor = Motor(Port.A, Direction.CLOCKWISE)
minimotor = Motor(Port.A, Direction.CLOCKWISE)
button = TouchSensor(Port.S1)
#color = ColorSensor(Port.S4)
#robot = DriveBase(right_motor, left_motor,  )
direction =1
while True:
    #print(color.rgb())
    if button.pressed():
        direction = direction *-1
    minimotor.run(direction*40)
    #left_motor.run(direction*0)
'''
while True:
    sangle = stationary.angle() 
    rangle = rotating.angle()
    while button.pressed():
        print('hi')
        rotating.run_target(1,1, stop_type=Stop.BRAKE)
    rotating.run_time(1,1, stop_type=Stop.COAST)
    fobj.write('Rotating,'+str(rangle)+ ',Stationary,'+ str(sangle)+'\n')
'''

fobj.close()