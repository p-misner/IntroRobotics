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
y2 =pd.to_numeric(df[3])
plt.scatter(time,y2)
plt.scatter(time,y1)

plt.ylim((0,800)