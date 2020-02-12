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

brick.sound.beep()

minimotor = Motor(Port.C)
leftmotor = Motor(Port.A, Direction.CLOCKWISE)
rightmotor= Motor(Port.D, Direction.CLOCKWISE)
robot = DriveBase(leftmotor,rightmotor, 40, 200)
button = TouchSensor(Port.S1)
color = ColorSensor(Port.S2)

#sense = AnalogSensor(Port.S3, False)
uart = UARTDevice(Port.S3, 9600, timeout=10000)
direction = 1

#initial waiting phase:

handshake = "f"
while uart.waiting() == 0:
    wait(10)

handshake = uart.read(1)
print(handshake)

while True:
    if uart.waiting() != 0:
        print(uart.read(1))
    
    wait(0.1)
