#!/usr/bin/env pybricks-micropython
#brickrun -r -- pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.iodevices import AnalogSensor, UARTDevice
def colorcheck():
    if color.color() != Color.WHITE:
        uart.write('b')
        print('LETTER')
    else:
        uart.write('a')

brick.sound.beep()
print("pls but sadder")
minimotor = Motor(Port.C)
leftmotor = Motor(Port.A, Direction.CLOCKWISE)
rightmotor= Motor(Port.D, Direction.CLOCKWISE)
robot = DriveBase(leftmotor,rightmotor, 40, 200)
#button = TouchSensor(Port.S1)
color = ColorSensor(Port.S1)

#sense = AnalogSensor(Port.S3, False)
uart = UARTDevice(Port.S4, 9600, timeout=1000)
direction = 1

#initial waiting phase:

handshake = "f"
while uart.waiting() == 0:
    wait(10)
print('b4')
handshake = uart.read(1)
print('hi',len(handshake))
holder = b'a'
motorspeed = 0
minispeed = 0
while True:
    colorcheck()
    if uart.waiting() != 0:
        holder = uart.read(1).decode("utf-8")
        print(holder)
        if holder == 'y': #forward
            motorspeed = 20
            minispeed = 0
        elif holder == 'u': #backward
            motorspeed = -20
            minispeed = 0
        elif holder == 's': #left
            minispeed = -20
            motorspeed = 0
        elif holder == 'w': #right
            minispeed = 20
            motorspeed = 0
        elif holder == 'x': # diagonal up right
            minispeed = 20
            motorspeed = 20
        elif holder == 'z': # diagonal up left
            minispeed = -20
            motorspeed = 20
        elif holder == 't': # diagonal down left
            minispeed = -20
            motorspeed = -20
        elif holder == 'v': # diagonal down right
            minispeed = 20
            motorspeed = -20
        else: # q; middle
            motorspeed = 0
            minispeed = 0
        
        ''' if color.color() != Color.WHITE:
            uart.write('b')
            print('LETTER')
        else:
            uart.write('a')'''
   
    


    robot.drive(motorspeed,0)
    minimotor.run(minispeed)
    wait(0.1)
