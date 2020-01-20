#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
#brick.sound.beep()

right_motor = Motor(Port.B, Direction.CLOCKWISE)
left_motor = Motor(Port.A, Direction.CLOCKWISE)
light = ColorSensor(Port.S3)
rtouch = TouchSensor(Port.S4)
ltouch = TouchSensor(Port.S2)

'''
#run_time(speed, time, stop_type=Stop.COAST, wait=True)
running = True
while running == True:
    #motor spins in back and forth circles
    right_motor.dc(100)
    right_motor.run_angle(1000,30, Stop.COAST, True)
    left_motor.run_angle(1000,-30, Stop.COAST, True)

    #light sensor
    #stays on the table, constantly moving
'''
def moveBack():
    print('BACK CALLED')
    left_motor.run_time(-180,2000,Stop.COAST, True)
    right_motor.run_time(-180,2000,Stop.COAST, True)
    turn(90)
def moveForward():
    
    left_motor.run(180)
    right_motor.run(180)

def turn(turn_angle):
    if (checkReflection() > 10):
        left_motor.run_angle(60,turn_angle,Stop.COAST,True)
        #right_motor.run_angle(60,-turn_angle,Stop.COAST,True)
    

def checkReflection():
    reflect = light.ambient()
    
    if reflect>13:
        #on the table
        return(True)
    else:
        return(False)

''' START HERE '''

while True:
    onTable = checkReflection()
    sideOn = rtouch.pressed() or ltouch.pressed()
    if sideOn == False:
        brick.sound.beep()
    if ((sideOn == True) and (onTable == True)):
        right_motor.run(90)
        left_motor.run(90)
    else:
        print("OFF TABLE")
        moveBack()



