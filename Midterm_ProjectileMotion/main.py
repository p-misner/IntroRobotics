#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import math 
# Write your program here
brick.sound.beep()

def dsin(val):
    return math.sin(math.radians(val))
def dcos(val):
    return math.cos(math.radians(val)) 
def calcv0(d,theta,h):
    v0 = pow(((g*d*d)/(2*d*dsin(theta)*dcos(theta)+2*h*dcos(theta)*dcos(theta))),0.5)
    return v0
def dcconvert(x):
    print(77.9 - 15.7*x+19.4*x**2)
    return 77.9 - 15.7*x+19.4*x**2










throw = Motor(Port.A, Direction.COUNTERCLOCKWISE)
#throwback= Motor(Port.A, Direction.CLOCKWISE)
ultra = UltrasonicSensor(Port.S1)
btn = TouchSensor(Port.S2)
angle = 137
d= float(ultra.distance())/1000
h = 9*2.54/100
g= 9.81
theta = 47.5

while True:
    d= float(ultra.distance())/1000 + 1.75*2.54/100
    speed =dcconvert(calcv0(d,theta,h))
    print(speed)
    offset = (throw.angle())
    #print(ultra.distance())
    if btn.pressed(): 
        for i in range(1000):
            if abs(throw.angle())< abs(115):
                throw.dc(speed)
            else:
                break
            wait(0.1)
        print('done')

        throw.run_angle(2,2,stop_type=Stop.COAST, wait=True)
        # wait(1000)
        # # throw.run_angle(100,-1*angle/2,stop_type=Stop.COAST, wait=True)
