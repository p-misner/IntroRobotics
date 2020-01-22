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
#small = Motor(Port.C, Direction.COUNTERCLOCKWISE)
robot = DriveBase(left_motor,right_motor,56,160)
light = ColorSensor(Port.S3)
ultra = UltrasonicSensor(Port.S2)
#rtouch = TouchSensor(Port.S4)
#touch = TouchSensor(Port.S2)


def checkReflection():
    reflect = light.ambient()
    if reflect>13:
        #on the table
        return(True)
    else:
        return(False)

# Establishing counter values
l_counter = 0
r_counter = 0

while True:
    # Defining sensor variables
    onTable = checkReflection()
    #l_sideOn = ltouch.pressed()
    #r_sideOn = rtouch.pressed()
    
    #currangle = (small.angle())%365
    print(ultra.distance())
    '''
    if currangle < 180:
        small.run(75)
    else:
        small.run(-75)
    '''
    
    
    #print("Light Sensor is ", onTable)
    #print("Right Side is ", r_sideOn)
    #print("Left Side is ", l_sideOn)
   
    if onTable == True:
        if (ultra.distance() <300):
            robot.drive(200,0)
        else: 
            robot.drive(100,0)
    elif onTable == False:
        robot.drive_time(-100,70,2000)
    
        
      
        
    '''
    #In the case that only the left limit switch runs off (shallow angle of approach)
    if (l_sideOn == False):
        #brick.sound.beep()
        if (onTable == True):
            left_motor.run_target(300,-1200)
        else: 
            right_motor.run(0)
            left_motor.run_time(-180,2000,Stop.COAST, True)

    #In the case that only the right limit switch runs off (shallow angle of approach)
    elif (r_sideOn == False):
        #brick.sound.beep()
        if (onTable == True) and (l_sideOn == True):
            left_motor.run(-180)
        else: 
            left_motor.run(-180)
        
        

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
'''