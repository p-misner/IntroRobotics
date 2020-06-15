#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

#For Serial communication:
from pybricks.parameters import Color, Port
from pybricks.iodevices import AnalogSensor, UARTDevice, I2CDevice
from serial import Serial
import ubinascii, ujson, urequests, utime
import time
# Write your program here
brick.sound.beep()

motor = Motor(Port.A, Direction.CLOCKWISE)
left = Motor(Port.D, Direction.CLOCKWISE)
right = Motor(Port.C, Direction.CLOCKWISE)
robot = DriveBase(left, right, 56, 76.2)
uart = UARTDevice(Port.S1, 9600, timeout=2000)
print(motor.angle())

Key = 'bvd8X9LweQY9o2eP1NYL-p8mLL9wMAk6YYOnYSiIo0'
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

def read_serial():
	try:
		if (uart.waiting()) !=0:
			print('hiii')
			msg = uart.read(uart.waiting()).decode('utf-8')
			print(msg)
			return msg
	except Exception as e:
		print(e)
		#continue
def write_serial(msg):
	uart.write(str(msg).encode())
def driveback():
	robot.drive(-60,0)
	wait(5000)
	robot.drive(0,0)
count = 0
end = True
print('start')
while True:
	run = Get_SL('Start04')
	wait(1000)
	print(run)
	while run == 'true':
		rec = read_serial()
		if (rec == 'n'):
			end = False
			print(rec)
		elif (rec == 'd'):
			end = True
			driveback()
		elif (rec == 'w' or rec == 'wd') :
			end = True
			driveback()
			Put_SL('Start04', 'BOOLEAN', 'false')
			Put_SL('Start05', 'BOOLEAN', 'true')

		if (end == False ):
			robot.drive(10,1)
			if (rec == 'j'):
				print(rec)
				motor.run_angle(-80,200,Stop.COAST, True)
				motor.run_angle(80,200,Stop.COAST, True)

	# write_serial('1')
	# print(rec)
	# if (str(rec) == '2'):
	# 	uart.write(str(3).encode())
	# count = count+1
	# wait(1000)
	# robot.drive(50,0)
	# wait(4000)
	# robot.drive(0,0)
	# motor.run_angle(-100,310,Stop.COAST, True)
	# motor.run_angle(100,310,Stop.COAST, True)

	# run = Get_SL('Start04')
	# wait(1000)
	# print(run)
	# while(run == 'true'):
	# 	count = count + 1
	# 	motor.run_angle(20,100,Stop.COAST, True)
	# 	print(motor.angle())
	# 	robot.drive(50,0)
	# 	wait(1000)
	# 	robot.drive(0,0)
	# 	run = Get_SL('Start04')
	# 	if (count >1):
	# 		Put_SL('Start04', 'BOOLEAN', 'false')


















# uart = UARTDevice(Port.S4, 9600, timeout=2000)

# def read():
# 	try:
# 		print(uart.waiting())
# 		if (uart.waiting()) !=0:
# 			msg = uart.read(uart.waiting()).decode('utf-8')
# 			print(msg[-1])
# 			return msg[-1]
# 	except Exception as e:
# 		print(e)
# 		#continue
# def write(message):
# 	uart.write(str(message).encode())

# i2c = I2CDevice(Port.S4,0x04 )
# while True:
# 	i2c.write(4, b'h')
# 	i2c.write(4, b'e')
# 	i2c.write(4, b'l')
# 	i2c.write(4, b'p')

# 	wait(1000)
# 	print('round done')





