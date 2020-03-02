
from pybricks.hubs import EV3Brick
from pybricks.parameters import Color, Port
from pybricks.ev3devices import (Motor, TouchSensor,
          ColorSensor, UltrasonicSensor, GyroSensor)
from pybricks.tools import wait, StopWatch
import random, math

# Initialize the EV3
ev3 = EV3Brick()
ev3.speaker.beep()

touch = TouchSensor(Port.S2)
timer = StopWatch()
categories = [75,75,75,80,80,80,85,85,85,90,90,90,95,95,95]

distance = [32,49,68,139,157,145,199,209,197,243,259,250,298,290,302]
np.sum(distance)
def KNN(cat1, cat2, x, k):
     dist = []
     for data in cat1:
          dist.append((abs(x-data),0))
     for data in cat2:
          dist.append((abs(x-data),1))
     dist.sort()     
     sum = 0
     for i in range(k):
          sum += dist[i][1] 
     return 0 if sum < (k-sum) else 1  # return 0 if mostly 0s