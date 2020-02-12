#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 15:29:15 2020

@author: priyamisner
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
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
filename ='./error.csv'
fin = open(filename,'r')
data = []
for line in fin:    
    line = line.split(',')
    data.append(line)

df= pd.DataFrame(data)

time = np.arange(len(df))
for num in df[1]:
    num = int(num) + 60
for num in df[3]:
    num = int(num) + 60
rotating  = pd.to_numeric(df[1])
stationary = pd.to_numeric(df[3])

#left
plt.scatter(stationary,rotating,c='r')
plt.xlabel('Stationary')
plt.ylabel('Rotating')
#right

#left deriv
#plt.scatter(time,y9,c='y')
#right deriv
#plt.scatter(time,y11,c='g')
#plt.scatter(time,y13)




plt.ylim((-200,200))

#left deriv
#plt.scatter(time,y9,c='y')
#right deriv
#plt.scatter(time,y11,c='g')
#plt.scatter(time,y13)
