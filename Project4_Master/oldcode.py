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

minimotor = Motor(Port.D)
leftmotor = Motor(Port.C, Direction.CLOCKWISE)
rightmotor= Motor(Port.B, Direction.CLOCKWISE)
robot = DriveBase(leftmotor,rightmotor, 40, 200)
button = TouchSensor(Port.S1)
color = ColorSensor(Port.S2)

#sense = AnalogSensor(Port.S3, False)


direction = 1

while True:
    if button.pressed():
        direction *= -1
    minimotor.run(direction*20)
    robot.drive(direction*0,0)
    data = color.color()
    #uart.write(data)
    wait(500)
    #print(color.color())







'''
from pybricks.hubs import EV3Brick
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.parameters import Color, Port
from pybricks.ev3devices import Motor
from pybricks.iodevices import AnalogSensor, UARTDevice

# Initialize the EV3
ev3 = EV3Brick()
ev3.speaker.beep()
sense = AnalogSensor(Port.S3, False)
uart = UARTDevice(Port.S3, 9600, timeout=2000)


#watch = StopWatch()

# Turn on a red light
ev3.light.on(Color.BLUE)
ev3.speaker.say("About to take data")
count = 0
while True:
    wait(1000)
    data = uart.read_all()  #if you connect Pin 5 & 6 you should see Test on the screen
    count += 1
    ev3.screen.print(count,data)
'''