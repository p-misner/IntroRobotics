#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import ubinascii, ujson, urequests, utime, random


# Write your program here
brick.sound.beep()
Key ='AurMcNakEofCjunPMcNKT4P_eWCNcmDs6dVU_8zHoD'
#Key = 'MSDnMb7QQV3FrnkCysYgfmNxHgpRu1dxaVqEXxEDWD'

def SL_setup():
		 urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
		 headers = {"Accept":"application/json","x-ni-api-key":Key}
		 return urlBase, headers
def Put_SL(Tag, Type, Value):
		 urlBase, headers = SL_setup()
		 urlValue = urlBase + Tag + "/values/current"
		 propValue = {"value":{"type":Type,"value":Value}}
		 try:
					reply = urequests.put(urlValue,headers=headers,json=propValue).text
		 except Exception as e:
					print(e)
					reply = 'failed'
		 return reply
def Get_SL(Tag):
		 urlBase, headers = SL_setup()
		 urlValue = urlBase + Tag + "/values/current"
		 try:
					value = urequests.get(urlValue,headers=headers).text
					data = ujson.loads(value)
					#print(data)
					result = data.get("value").get("value")
		 except Exception as e:
					print(e)
					result = 'failed'
		 return result
    
bigArm = Motor(Port.D, Direction.CLOCKWISE)
tilt = Motor(Port.A,Direction.CLOCKWISE)
turn = Motor(Port.B, Direction.CLOCKWISE)
btn = TouchSensor(Port.S1)
while True:
    direc = 1
    indexNum = int(Get_SL('ImageNum'))
    #print(indexNum)
    #print(type(indexNum))
    # print(int(indexNum))
    if indexNum != 6:
        # move arm to bins
        bigArm.run_angle(20, 42*direc, Stop.COAST, wait=True)
        wait(100)
        # rotate bins
        turn.run_angle(20, 72*indexNum*direc, Stop.COAST, wait=True)
        wait(100)
        # dump brick  
        tilt.run_angle(20, -70*direc, Stop.COAST, wait=True)
        wait(100)
        # change direction
        direc = -1
        # tilt arm back
        tilt.run_angle(20, -70*direc, Stop.COAST, wait=True)
        # rotate bins back
        turn.run_angle(20, 72*indexNum*direc, Stop.COAST, wait=True)
        # move big arm back
        bigArm.run_angle(20, 42*direc,Stop.COAST, wait=True)
        # wait for button
        while btn.pressed() != True:
            wait(100)
        brick.sound.beep()
        Put_SL('ImageNum', 'STRING','6')
        