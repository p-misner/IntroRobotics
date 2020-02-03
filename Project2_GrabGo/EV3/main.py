#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import ubinascii, ujson, urequests, utime
# Write your program here
brick.sound.beep()
 '''    
Key = 'fnqbuA49ZzUBEYS8k1PdSTNv6FNgDXx32PUCBm_u8B'
#Key = 'zAZnvs9_lRUgQLtciuSuMHSNoqURxyWldeb7Q_EsRs' 
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
     
def Create_SL(Tag, Type):
     urlBase, headers = SL_setup()
     urlTag = urlBase + Tag
     propName={"type":Type,"path":Tag}
     try:
          urequests.put(urlTag,headers=headers,json=propName).text
     except Exception as e:
          print(e)
'''      
#Get_SL('Bill')
#Create_SL('Bill','STRING')
#Put_SL('Bill','STRING','done')
#Get_SL('Bill')
left_motor = Motor(Port.A)
#right_motor = Motor(Port.D)
#while True:
    #speed = Get_SL('moveforward')
    #brick.display.text(speed, Align.CENTER)
   
    #left_motor.run(int(speed))
   # wait(1000)