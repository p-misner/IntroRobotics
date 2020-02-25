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
def colorcheck(side,up,direction):
    if color.color() != Color.WHITE:
        if direction == -1:
            side = 80 -side
        fobj.write(str(side)+','+str(up)+'\n')
    else:
        uart.write('a')

brick.sound.beep()
minimotor = Motor(Port.C)
leftmotor = Motor(Port.A, Direction.CLOCKWISE)
watch = StopWatch()
watchside = StopWatch()
rightmotor= Motor(Port.D, Direction.CLOCKWISE)
robot = DriveBase(leftmotor,rightmotor, 40, 200)
color = ColorSensor(Port.S1)

uart = UARTDevice(Port.S4, 9600, timeout=1000)
direction = 1

#initial waiting phase:
holder = b'a'
motorspeed = 0
minispeed = 0
filename = 'letters.csv'
fobj = open(filename, 'w')
for up in range(20):
    print(up)
    watch.reset()
    watch.resume()
    while watch.time() < 200:
        robot.drive(20, 0)
    robot.drive(0,0)
    for side in range(80):
        watchside.reset()
        watchside.resume()
        while watchside.time()<150:
            minimotor.run(direction*-50)
            colorcheck(side,up,direction)
    direction *= -1
while True:
    colorcheck()
    direction = 1
    if uart.waiting() != 0:
        holder = uart.read(1).decode("utf-8")
        print(holder)
        if holder == 'q': #forward
            motorspeed = 0
            minispeed = 0

    #robot.drive(motorspeed,0)
    #minimotor.run(minispeed)
    
    wait(0.1)
fobj.close()
