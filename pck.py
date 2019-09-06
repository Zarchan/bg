# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:06:11 2019

@author: chandlerzach
"""


import matplotlib.pyplot as plt
import numpy as np
import pickle
from scipy.signal import find_peaks
import functools

f = open("pickle","rb")
time = pickle.load(f)
data = pickle.load(f)


plt.figure(figsize=(18,16))
pivot = [data[:,i] for i in range(len(data[0]))]
z_peaks = functools.partial(find_peaks,height=.2, distance=100)
#peaks, thing = find_peaks(pivot[7], height = 0.2, distance = 100)
results = list(map(z_peaks,pivot))
peaks = [results[i][0] for i in range(len(results))]
heights = [results[i][1] for i in range(len(results))]

plt.subplot(2,1,1)
plt.axis([0,6,-.2,0.6])
plt.plot(time,data[:,0])
plt.subplot(2,1,2)
plt.axis([0,6,-.2,0.6])
plt.plot(time,data)

a = [i/1000 for j in peaks for i in j]
b = [heights[i]["peak_heights"] for i in range(len(heights))]
b = [i for j in b for i in j]
plt.plot(a,b,"*")




