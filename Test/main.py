#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import ubinascii, ujson, urequests, utime
import time, math
import ubinascii, ujson, urequests, utime, random
     
# pw = []
# with open('env_file.txt', 'r') as f:
#    for line in f:
#         key, value = line.strip().split('=', 1)
#         string1 = '{"name":"' +key+ '","value":"'+value+'"}'
#         pw.append(string1)
# pw = ujson.loads(pw[0])
Key = "BIpUblKc0qPQQEybX_xwoQ1PrUIN9fpZ60-DqjVVcT"
     
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
def takeSecond(elem):
    return elem[0]
def l_interp(dist,val):
    i = categories.index(dist[1])
    if i == 0 or i==(len(categories)-1):
        speed = categories[i]
    else:
        above_below =  1 if val - distance[i] >= 0 else -1 
        x0 = distance[i + above_below]
        x1 = distance[i]
        y0 = categories[i + above_below]
        y1 = categories[i]
        x = val
        speed = (y0*(x1-x)+y1*(x-x0))/(x1 -x0)
    return(speed)
def KNN(categories, distance, x, k):
    dist = []
    for (i, val) in enumerate(distance):
        dist.append((abs(val-x),categories[i]))
    dist.sort(key=takeSecond)
    return(l_interp(dist[0],x))

    
    #this is actual k means
    # return 0 if sum < (k-sum) else 1  # return 0 if mostly 0s
def dsin(val):
    return math.sin(math.radians(val))
def dcos(val):
    return math.cos(math.radians(val)) 
def calcv0(d,theta,h):
    v0 = pow(((g*d*d)/(2*d*dsin(theta)*dcos(theta)+2*h*dcos(theta)*dcos(theta))),0.5)
    return v0
def dcconvert(x):
    print(77.9 - 15.7*x+19.4*x**2)
    return 77.9 - 15.7*x+19.4*x**2
#Define Sensors
ultra= UltrasonicSensor(Port.S1)
throw = Motor(Port.A, Direction.COUNTERCLOCKWISE)
turn = Motor(Port.D, Direction.COUNTERCLOCKWISE)

# #Training Data
# categories = [73,75, 80, 85,90,95, 100 ]
# distance = [32,51,139,200, 247, 290, 310]
# for i,val  in enumerate(distance):
#     distance[i] = val 
#Constants
angle = 137
d= float(ultra.distance())/1000
h = 9*2.54/100
g= 9.81
theta = 47.5

while True:
    go = Get_SL('Throw')
    spin = Get_SL('Spin')
    # speed = KNN(categories,distance,ultra.distance() ,3) -1
    speed =dcconvert(calcv0(float(ultra.distance())/1000 + 1.75*2.54/100,theta,h)) -2
    print(ultra.distance(), '         ',speed)
    if go == 'true' : 
        Put_SL('distance', 'STRING',str(float(ultra.distance())/10) + ' cm')
        Put_SL('speed', 'STRING',str(speed)[:4]+ '%')
        Put_SL('Throw', 'BOOLEAN','false')
        wait(500)
        for i in range(1000):
            if abs(throw.angle())< abs(115):
                throw.dc(speed)
            else:
                break
            wait(0.1)
        print('done')
        throw.run_angle(2,2,stop_type=Stop.COAST, wait=True)
    
    
    if spin != 0:
        print(spin)
        turn.run_angle(50,int(spin),stop_type=Stop.COAST, wait=True) 
        Put_SL('Spin', 'INT','0')
        wait(500)





