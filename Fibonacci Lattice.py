# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 19:25:43 2020

@author: Alyssa
"""

import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (6,6)
plt.rcParams['figure.dpi'] = 150

from mpl_toolkits.mplot3d import Axes3D

phi = (1+math.sqrt(5))/2
N = 25
radius = 1

coordinates = []
X = []
Y = []
Z = []

# Constructing the spiral lattice

for i in range(-N, N+1):
    lat = math.asin(2*i/(2*N+1))*(180/np.pi)
    lon = (i % phi)*360/phi
    
    if lon < -180:
        lon = 360 + lon
    if lon > 180:
        lon = lon - 360
    
    vPhi = (90-lat)*(np.pi/180)
    theta = (lon+180)*(np.pi/180)

    x,y,z = -((radius)*math.sin(vPhi)*math.cos(theta)), ((radius)*math.cos(vPhi)), ((radius)*math.sin(vPhi)*math.sin(theta))
    
    X.append(x)
    Y.append(y)
    Z.append(z)
    
    coordinates.append((x,y,z))
    
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(X,Y,Z, s=4)

# Creating adjacent dictionary

def distance(v1, v2):
    return round(math.sqrt((v1[0]-v2[0])**2+(v1[1]-v2[1])**2+(v1[2]-v2[2])**2), 2)
bx,by,bz = [], [], []
Ax, Ay, Az = [], [], []

d = 0.56
adj = {}

for i in coordinates:
    adj[i] = []
    for j in coordinates:
        if distance(i,j) <= (d+0.5) and distance(i,j) >= (d+0.3):
            adj[i].append(j)
