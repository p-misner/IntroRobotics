# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
filename ='./error.csv'
fin = open(filename,'r')
data = []
for line in fin:    
    line = line.split(',')
    print(line)
    data.append(line)

df= pd.DataFrame(data)

time = np.arange(len(df))
y1 = pd.to_numeric(df[1])
y3 =pd.to_numeric(df[3])
y5 =pd.to_numeric(df[5])
y7 =pd.to_numeric(df[7])
y9 = pd.to_numeric(df[9])
y11 = pd.to_numeric(df[11])
y13 = pd.to_numeric(df[13])
#left
plt.scatter(time,y3,c='r')
#right
plt.scatter(time,y1, c='b')
#left integ
plt.plot(time,y5,c='m')
#right integ
plt.plot(time,y7, c='m')

#left deriv
#plt.scatter(time,y9,c='y')
#right deriv
#plt.scatter(time,y11,c='g')
#plt.scatter(time,y13)




plt.ylim((-500,500))