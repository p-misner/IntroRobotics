#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 08:45:13 2020

@author: priyamisner
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
filename ='./letters.csv'
fin = open(filename,'r')
data = []
for line in fin:    
    line = line.split(',')
    print(line)
    data.append(line)

df= pd.DataFrame(data)

time = np.arange(80)
y1 = pd.to_numeric(df[0])
y3 =pd.to_numeric(df[1])

#left
plt.scatter(y1,y3,c='r')
#right
#plt.scatter(time,y1, c='b')
#left integ

#left deriv
#plt.scatter(time,y9,c='y')
#right deriv
#plt.scatter(time,y11,c='g')
#plt.scatter(time,y13)




plt.xlim((0,80))