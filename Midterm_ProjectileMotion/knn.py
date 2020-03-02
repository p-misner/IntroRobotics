#!/usr/bin/env pybricks-micropython

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

brick.sound.beep()

touch = TouchSensor(Port.S2)
ultra= UltrasonicSensor(Port.S1)
throw = Motor(Port.A, Direction.COUNTERCLOCKWISE)
 

def takeSecond(elem):
    return elem[0]
def KNN(categories, distance, x, k):
    dist = []
    for (i, val) in enumerate(distance):
        dist.append((abs(val-x),categories[i]))
        dist.sort(key=takeSecond)

    sum = 0
    for i in range(3):
        sum += dist[i][1] 
    return(sum/3)
    #this is actual k means
    # return 0 if sum < (k-sum) else 1  # return 0 if mostly 0s

categories = [75,75,75,80,80,80,85,85,85,90,90,90,95,95,95]
distance = [32,49,68,139,157,145,199,209,197,243,259,250,298,290,302]
while True:
    speed = KNN(categories,distance,ultra.distance() + 100 ,3)
    if touch.pressed(): 
        for i in range(1000):
            if abs(throw.angle())< abs(115):
                throw.dc(speed)
            else:
                break
            wait(0.1)
        print('done')
        throw.run_angle(2,2,stop_type=Stop.COAST, wait=True)
