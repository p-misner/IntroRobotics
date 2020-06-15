#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import math 

# Initialize the EV3

# brick.sound.beep()

touch = TouchSensor(Port.S2)
ultra= UltrasonicSensor(Port.S1)
throw = Motor(Port.A, Direction.COUNTERCLOCKWISE)
 

def takeSecond(elem):
    return elem[0]

def l_interp(dist,val):
    i = categories.index(dist[1])
    if i == 0 or i==(len(categories)-1):
        speed = categories[i]
    else:
        above_below =  1 if val - distance[i] >= 0 else -1 
        x0 = distance[i + above_below]
        x1 = distance[i]
        y0 = categories[i + above_below]
        y1 = categories[i]
        x = val
        speed = (y0*(x1-x)+y1*(x-x0))/(x1 -x0)
    return(speed)
def KNN(categories, distance, x, k):
    dist = []
    for (i, val) in enumerate(distance):
        dist.append((abs(val-x),categories[i]))
    dist.sort(key=takeSecond)
    return(l_interp(dist[0],x))

    
    #this is actual k means
    # return 0 if sum < (k-sum) else 1  # return 0 if mostly 0s

categories = [73,75, 80, 85,90,95, 100 ]
distance = [32,51,139,200, 247, 290, 310]
for i,val  in enumerate(distance):
    distance[i] = val 
while True:
    speed = KNN(categories,distance,ultra.distance() ,3)
    print(ultra.distance(), '         ',speed)
    if touch.pressed(): 
        for i in range(1000):
            if abs(throw.angle())< abs(115):
                throw.dc(speed)
            else:
                break
            wait(0.1)
        print('done')
        throw.run_angle(2,2,stop_type=Stop.COAST, wait=True)

