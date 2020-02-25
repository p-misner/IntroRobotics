import numpy as np
import cv2
import PIL.Image
from io import BytesIO
import IPython.display
import imutils
import serial
s = serial.Serial("/dev/serial0",9600,timeout=2000)
s.write("begin".encode()) #to write to EV3

cap = cv2.VideoCapture(0)
d1 = IPython.display.display("Your image will be displayed here", display_id=3)
d2 = IPython.display.display("Your image will be displayed here", display_id=4)

def array_to_image(a, fmt='png'):
	f = BytesIO()
	PIL.Image.fromarray(a).save(f, fmt)
	return IPython.display.Image(data=f.getvalue())

def colorchoice(angle):
	#reds
	lower_red = np.array([150,50,50])
	upper_red = np.array([180,255,255])
	lower_red2 = np.array([170,50,50])
	upper_red2 = np.array([180,255,255])

	#green
	lower_g= np.array([40,80,20])
	upper_g= np.array([70,255,255])

	#range of blues
	lower_blue = np.array([95,80,50])
	upper_blue = np.array([125,255,255])

	#yellow
	lower_y= np.array([26,80,20])
	upper_y= np.array([35,255,255])

	#masks
	maskred = cv2.inRange(hsv, upper_red, lower_red)+ cv2.inRange(hsv, lower_red2, upper_red2)
	maskgreen = cv2.inRange(hsv, lower_g, upper_g)
	maskyellow = cv2.inRange(hsv, lower_y, upper_y)
	maskblue = cv2.inRange(hsv, lower_blue, upper_blue)

	mask = maskred
	if (abs(angle)>= 0 and abs(angle)<90):
			mask = maskred
	elif (abs(angle) >= 90 and abs(angle)<180):
			mask = maskblue
	elif (abs(angle) >=180 and abs(angle)<270):
			mask = maskyellow
	elif (abs(angle >=270 and abs(angle)<360)):
			mask = maskgreen
	return(mask)

toSend = 0
complete = False
angle = 0
while True:
	if (s.inWaiting()) != 0:
		#print('SINWAITING: ', str(s.inWaiting()))
		msg = s.read(s.inWaiting()).decode('utf-8')
		#print(int(msg)%360)
		angle = int(msg)%360
	# Capture frame-by-frame and convert to hsv
	ret, frame = cap.read()
	frame = imutils.resize(frame, width=200, inter=cv2.INTER_LINEAR)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	mask = colorchoice(angle)
	d1.update(array_to_image(mask))
	#d2.update(array_to_image(hsv))
	if np.sum(mask) > 100:
		toSend = 1
	else:
		toSend = 0
	complete = True
	if complete==True:
		s.write(str(toSend).encode()) #to write to EV3
	complete = False



# When everything done, release the capture
cap.release()