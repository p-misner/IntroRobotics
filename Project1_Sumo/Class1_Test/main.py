#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here

right_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
light = ColorSensor(Port.S3)
rtouch = TouchSensor(Port.S4)
ltouch = TouchSensor(Port.S2)

def moveBack_left():
    print('BACK CALLED')
    left_motor.run_time(180,2000,Stop.COAST, True)
    right_motor.run_time(-180,2000,Stop.COAST, True)
    #turn(90)
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
# Establishing counter values
l_counter = 0
r_counter = 0

while True:

    # Defining sensor variables
    onTable = checkReflection()
    l_sideOn = ltouch.pressed()
    r_sideOn = rtouch.pressed()
    
    print("Light Sensor is ", onTable)
    print("Right Side is ", r_sideOn)
    print("Left Side is ", l_sideOn)
    print(checkReflection())
    while True:
        left_motor.run_target(300,1200)
        
    
    #In the case that only the left limit switch runs off (shallow angle of approach)
    if (l_sideOn == False):
        #brick.sound.beep()
        if (onTable == True):
            right_motor.run_time(-180,10,Stop.COAST, True)
            left_motor.run_time(-180,2000,Stop.COAST, True)
        else: 
            right_motor.run(0)
            left_motor.run_time(-180,2000,Stop.COAST, True)

    #In the case that only the right limit switch runs off (shallow angle of approach)
    elif (r_sideOn == False):
        #brick.sound.beep()
        if (onTable == True) and (l_sideOn == True):
            left_motor.run_time(-180,100,Stop.COAST, True)
            right_motor.run_time(-180,2000,Stop.COAST, True)
        else: 
            left_motor.run(0)
            right_motor.run_time(-180,2000,Stop.COAST, True)
        
        

    #In the case of failure of readout from the light sensor
    elif (l_sideOn == False) and (r_sideOn == False):
        #brick.sound.beep()
        left_motor.run(-180,2000,Stop.COAST, True)
        right_motor.run(-180,2000,Stop.COAST, True)

    #In the case that the robot is headed directly to the edge of the table
    elif (onTable == False):
        #brick.sound.beep()
        left_motor.run_time(-180,2000,Stop.COAST, True)
        right_motor.run_time(180,2000,Stop.COAST, True)
 
    elif (onTable == False) and (l_sideOn == False):
        brick.sound.beep()
        right_motor.run(0)
        left_motor.run_time(-180,2000,Stop.COAST, True)


    # Moving case if the robot is on contact on the table
    elif (((l_sideOn == True) and (r_sideOn == True)) and (onTable == True)):
        right_motor.run(200)
        left_motor.run(200) 
