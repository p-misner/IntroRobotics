import cv2
import PIL.Image
from io import BytesIO
import IPython.display
import imutils

def array_to_image(a, fmt='jpeg'):
    f = BytesIO()
    PIL.Image.fromarray(a).save(f, fmt)    
    return IPython.display.Image(data=f.getvalue())

import numpy as np

cap = cv2.VideoCapture(0)
d1 = IPython.display.display("Your image will be displayed here", display_id=3)
d2 = IPython.display.display("Your image will be displayed here", display_id=4)
imagearray = []
def array_to_image(a, fmt='png'):
    f = BytesIO()
    PIL.Image.fromarray(a).save(f, fmt)    
    return IPython.display.Image(data=f.getvalue())

print("started")
for i in range(1):
    print(i)
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=200, inter=cv2.INTER_LINEAR)
    
    r = frame.copy()
    r[:, :, 1] = 0
    r[:, :, 0] = 0
    #Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #range of blues
    lower_blue = np.array([95,80,50])
    upper_blue = np.array([125,255,255])
    
    #range of reds
    lower_red = np.array([150,50,50])
    upper_red = np.array([180,255,255])
    lower_red2 = np.array([170,50,50])
    upper_red2 = np.array([180,255,255])
    
    #yellows
    lower_y= np.array([26,80,20])
    upper_y= np.array([35,255,255])
    
    #green
    lower_g= np.array([40,80,20])
    upper_g= np.array([70,255,255])
    
    
    # Threshold the HSV image to get only x colors
    maskblue = cv2.inRange(hsv, lower_blue, upper_blue) 
    maskred = cv2.inRange(hsv, upper_red, lower_red)
    maskyellow = cv2.inRange(hsv, lower_y, upper_y)
    maskgreen = cv2.inRange(hsv, lower_g, upper_g)
    maskred = maskred + cv2.inRange(hsv, lower_red2, upper_red2)

    # Bitwise-AND mask and original image
    #combine = cv2.bitwise_and(frame,frame, mask= mask)

    #d1.update(array_to_image(frame[100,100,0]))
    d1.update(array_to_image(maskred))
    d2.update(array_to_image(hsv))


# When everything done, release the capture
print('DONE')
cap.release()