
#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

from pybricks.ev3devio import Ev3devSensor 
import utime
import ev3dev2
from ev3dev2.port import LegoPort 


brick.sound.beep()
left_motor = Motor(Port.D, Direction.CLOCKWISE, [40,24])
right_motor = Motor(Port.A, Direction.CLOCKWISE, [40,24])
robot = DriveBase(left_motor,right_motor,56,202)
class MySensor(Ev3devSensor):  #Define Class 
    _ev3dev_driver_name="ev3-analog-01"
    def readvalue(self):
        self._mode('ANALOG')
        return self._value(0)

# Before running the code go to Device Browser and Sensors. Make sure you can see ev3-analog-01, otherwise you will get an error.
def control(right, left):
    direction = 1
    k_p = 0.5
    scale_factor = 0.005

    light_desired = 870
    rlightLevel = right
    rlight_desired = 870 #correct color sensor
    rerror = rlightLevel - rlight_desired
    llightLevel = left
    llight_desired = 1080
    lerror = llightLevel - llight_desired
    if (lerror > rerror):
        direction=1
        anglechange = direction*k_p*llightLevel*scale_factor
        return(anglechange)
    else:
        direction=-1
        anglechange = direction*k_p*rlightLevel*scale_factor
        return(anglechange)

# Write your program here
def main():
    brick.sound.beep()
    sens = LegoPort(address ='ev3-ports:in1') # which port?? 1,2,3, or 4
    sens.mode = 'ev3-analog'

    utime.sleep(0.5)
    sensor_left=MySensor(Port.S1) # same port as above
    sensor_right=MySensor(Port.S3) # same port as above

    robot.drive(0,0)
    while True:
        lightLevel = sensor_left.readvalue()
        lightLevel2 = sensor_right.readvalue() 

        print('Left',lightLevel,'Right', lightLevel2)
        robot.drive(1,control(lightLevel2,lightLevel))
        wait(200)

main()
