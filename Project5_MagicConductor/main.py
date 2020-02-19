#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks import ev3brick as brick
#from pybricks.ev3brick import sound
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from serial import Serial
import ujson
import math

# Write your program here
ev3 = EV3Brick()
#ev3.speaker.say('start')
brick.sound.beep(500,1000,20)
tare = TouchSensor(Port.S1)
wait(100)

def sign(val):
    if (val >= 0):
         return 1 
    else:
         return -1

def constrain(val, min, max):
    if val > max:
        return max
    elif val < min:
        return min 
    else:
        return val

def map(val, mode):
    if mode =='pitch':
        val = ((val + 180)/360 )*5000 + 600
        return val
    elif mode =='roll':
        val = ((val + 180)/360 )*3000 + 400
        return val
    elif mode=='flick':
        val = (val/1000)*90
        return val

def drum(roll):
    roll +=270
    begin = [0,120,240]
    end = [120,240,360]
    files = ['AcousticHat-06.wav','AcousticSnare-04.wav','cymbal-01.wav']
    for i in range(len(begin)):
        if roll >= begin[i] and roll <end[i]:
            return(files[i])
       
def main():
    s = Serial("/dev/ttyACM0", 9600)
    s2 = Serial("/dev/ttyACM1", 9600)
    iter = 0
    labels = ['xAcc', 'yAcc', 'zAcc', 'xGyro', 'yGyro', 'zGyro']
    x_gyro, y_gyro, z_gyro = 0, 0, 0
    while True:
        raw_data = s.read(s.inWaiting()).decode('utf-8')
        #raw_data2 = s2.read(s2.inWaiting()).decode('utf-8')
       
        if ((not 'zGyro' in raw_data)) :
            continue
        try:
            data = ujson.loads(raw_data)
            second = ujson.loads(raw_data2)
            for i,num in enumerate(data):
                data[labels[i]] = round((data[labels[i]]),2)
        except:
            continue
        
        pitch_direc= -1*sign(data['xAcc'])
        roll_direc = sign(data['zAcc'])
        pitch = pitch_direc*math.acos(constrain(data['zAcc'],-1,1))*180/math.pi
        roll = (roll_direc*math.acos(constrain(data['yAcc'],-1,1))*180/math.pi) -90
        
        #option 1 for control: settings
        freq = map(pitch,'pitch')
        brick.light(Color.RED)
        wait(700)
        brick.light(Color.GREEN)
        wait(300)
        duration = map(roll,'roll')

        #option 2: drumsticks (needs 2 arduinos, 1 to set, 1 to play)
        flick_mag = math.pow((math.pow(data['yGyro'],2)+math.pow(data['zGyro'],2)+math.pow(data['xGyro'],2)),0.5)
        flick = []
        '''
        while  flick_mag > 200:
            # Read raw data
            raw_data = s.read(s.inWaiting()).decode('utf-8')
            if not 'zGyro' in raw_data:
                continue
            try:
                data = ujson.loads(raw_data)
            except:
                continue
            
            flick_mag = math.pow((math.pow(data['yGyro'],2)+math.pow(data['zGyro'],2)+math.pow(data['xGyro'],2)),0.5)
            if flick_mag > 70:
                flick.append(flick_mag)
        #print(flick)
        '''
        mag = 1
        if len(flick)>0:
            length = len(flick)
            mag = int(map(max(flick),'flick'))
        print(drum(roll))

        #brick.sound.beep(freq, duration, 1)
        brick.sound.file(drum(roll),100)
        #brick.sound.say('words')
        wait(500)
        #print(data)




main()