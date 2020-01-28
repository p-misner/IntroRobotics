#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import ubinascii, ujson, urequests, utime
import time
# Write your program here
brick.sound.beep()


Key = 'rhMBtEV-N0ga9DQ4T6cJNblWQhAXGzBFn0XWU0hT6s'
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

def Get_RandomUseless():
    urlValue = 'https://uselessfacts.jsph.pl/random.json?language=en'
    try:
        value = urequests.get(urlValue).text
        data = ujson.loads(value)
        result = data.get("text")
    except Exception as e:
        print(e)
        result = 'FAILURE'
    return result  

def Create_SL(Tag, Type):
     urlBase, headers = SL_setup()
     urlTag = urlBase + Tag
     propName={"type":Type,"path":Tag}
     try:
          urequests.put(urlTag,headers=headers,json=propName).text
     except Exception as e:
          print(e)




#print(Get_SL('moveforward'))
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
box_motor = Motor(Port.C)

wheel_diameter =56
axle_track = 140
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

prevboxpos = 'false'

Put_SL('Stop','BOOLEAN','false')    
Put_SL('Straight','BOOLEAN','false')    
while True:
     speed = int(Get_SL('moveforward'))
     angle = int(Get_SL('TurnAngle'))

     stop = Get_SL('Stop')
     straight = Get_SL('Straight')
     boxpos = Get_SL('BoxPosition')
     newfact =Get_SL('NewFact')

     print(box_motor.angle())
     print("Prev", prevboxpos)
     print("Curr",boxpos)

     if (stop == 'true'):
          Put_SL('moveforward','INT','0')
          Put_SL('TurnAngle','INT','0')
          Put_SL('Stop','BOOLEAN','false')
     if (straight =='true'):
          Put_SL('TurnAngle','INT','0')
          Put_SL('Straight','BOOLEAN','false')
     if (newfact =='true'):
          uselessfacts = Get_RandomUseless()
          Put_SL('UselessFact','STRING',uselessfacts)
          Put_SL('NewFact','BOOLEAN','false')
     if (boxpos == 'true' and prevboxpos=='false'):
        print("Going Down")
        count= count +1
        box_motor.run_angle(50,-390,Stop.COAST, True)
     elif (boxpos == 'false' and prevboxpos=='true'):
        print("Going Up")
        count= count -1
        box_motor.run_angle(50,390,Stop.COAST, True)

     robot.drive(speed,angle)
     Put_SL('TurnAngle','INT','0')
     prevboxpos = boxpos
     

