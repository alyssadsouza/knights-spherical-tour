# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 11:46:39 2020

@author: Alyssa
"""
# ---------------------------------------------------------
# INITIAL SETUP

import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

phi = (1+math.sqrt(5))/2

plt.rcParams['figure.figsize'] = (6,6)
plt.rcParams['figure.dpi'] = 150

from mpl_toolkits.mplot3d import Axes3D

# Initial coordinates 

coordinates = [(0, 1, phi), (0, -1, phi), (0, 1, -phi), (0, -1, -phi),
                (1, phi, 0), (-1, phi, 0), (1, -phi, 0), (-1, -phi, 0),
                (phi, 0, 1), (-phi, 0, 1), (phi, 0, -1), (-phi, 0, -1)]
subdivision = 0

# Formatting coordinates for 3D axes in Python

x, y, z = [], [], []

for coord in coordinates:
    x.append(coord[0])
    y.append(coord[1])
    z.append(coord[2])
    
# Adjacent vertices

def theta(v1,v2):
    """
    Parameters
    ----------
    v1 : Tuple
        Vertex coordinates.
    v2 : Tuple
        Vertex coordinates.

    Returns
    -------
    theta : Float
        Angle between two vertices.
    """
    T = (v1[0]-v2[0], v1[1]-v2[1], v1[2]-v2[2])
    lenv1 = math.sqrt(v1[0]**2+v1[1]**2+v1[2]**2)
    lenv2 = math.sqrt(v2[0]**2+v2[1]**2+v2[2]**2)
    lenT = math.sqrt(T[0]**2+T[1]**2+T[2]**2)
    theta = abs(math.acos((lenv1**2+lenv2**2-lenT**2)/(2*lenv1*lenv2)))
    return theta

# two adjacent vertices (pre-determined) - their angles will serve as the comparison to determine adjacent pairs
p = (0,1,phi)
q = (phi,0,1)
a = math.degrees(theta(p, q))

adjac = {}

for v1 in coordinates:
    adjac[v1] = []
    for v2 in coordinates:
        b = math.degrees(theta(v1,v2))
        if b == a:
            adjac[v1].append(v2)

# ---------------------------------------------------------    
# SUBDIVISION

def Midpoint(v1, v2):
        """
        Parameters
        ----------
        v1 : Tuple
            Coordinates of vertex.
        v2 : Tuple
            Coordinates of vertex.
    
        Returns
        -------
        M : Tuple
            Coordinates of midpoint.
        """
        M = ((v1[0]+v2[0])/2, (v1[1]+v2[1])/2, (v1[2]+v2[2])/2)
        return M

def projectVertex(r, v):
        """
        Parameters
        ----------
        r : Float
            Radius of circumscribed sphere to project vertices on.
        v : Tuple
            Vertex coordinates (x, y, z).
    
        Returns
        -------
        Tuple containing projected vertex coordinates (x, y, z).
        """
        
        k = round(r/math.sqrt(v[0]**2+v[1]**2+v[2]**2),1)
        p = (k*v[0], k*v[1], k*v[2])
        
        return p

def subdivide(adjac):
    '''
    Parameters
    ----------
    adjac : dictionary
            Based off of graph, keys contain vertex numbers, 
            value contains list of adjacent vertices

    Returns
    -------
    None, displays vertices on a 3d plot
    '''
    # Displaying 3D axes
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    ax.scatter(x,y,z,s=4,c='r')
    
    # Finding midpoints
    
    midpoints = []
    
    adjacmid = {}
    for v1 in adjac.keys():
        for v2 in adjac[v1]:
            M = Midpoint(v1, v2)
            if M not in midpoints:
                midpoints.append(M)
                # add the points that are adjacent to the new point to a list
                adjacmid[M] = [v1, v2]
                # also add the midpoints between k, coord, and the only two points
                # that are adjacent to both k and coord
                twopts = []
                for i in adjac[v1]:
                    if i in adjac[v2]:
                        twopts.append(i)
                        
                A = Midpoint(v1, twopts[0])
                adjacmid[M].append(A)
                B = Midpoint(v1, twopts[1])
                adjacmid[M].append(B)
                C = Midpoint(v2, twopts[0])
                adjacmid[M].append(C)
                D = Midpoint(v2, twopts[1])
                adjacmid[M].append(D)
    
    # Project each midpoint to sphere and add to list of coordinates
    
    # (radius of circumscibed sphere)
    theta = 2*np.pi/5
    r = 2*(np.sin(theta))
    
    for v in midpoints:
        p = projectVertex(r, v)
        x.append(p[0])
        y.append(p[1])
        z.append(p[2])
        coordinates.append(p)
        
        # Project A B C D before adding to adjac[p] (first two points are already projected)
        adjacmid2 = adjacmid[v][:2]
        for i in adjacmid[v][2:]:
            a = projectVertex(r, i)
            adjacmid2.append(a)
        adjac[p] = adjacmid2
        
        adjac[adjacmid2[0]].remove(adjacmid2[1])
        adjac[adjacmid2[0]].append(p)
        
        adjac[adjacmid2[1]].remove(adjacmid2[0])
        adjac[adjacmid2[1]].append(p)
    
    midX = []
    midY = []
    midZ = []
    
    for v in midpoints:
        p = projectVertex(r, v)
        midX.append(p[0])
        midY.append(p[1])
        midZ.append(p[2])
    
    ax.scatter(midX,midY,midZ,s=4,c='r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

subdivide(adjac)
# # ---------------------------------------------------------