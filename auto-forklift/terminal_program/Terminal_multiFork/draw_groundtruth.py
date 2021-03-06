#!/usr/bin/env python
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

f = open("./map.txt")
x = []
y = []
for line in f:
    if line[0] == '#':
        continue
    data = line.split()
    x.append( float(data[0] ) )
    y.append( float(data[1] ) )
#ax = plt.subplot( 111,projection='3d')
ax = plt.subplot( 111)
ax.plot(x,y,color="g",linewidth=1.0)

#plt.xlim(-0.5,5.5)
#plt.ylim(-3.5,0.5)
#ax.set_zlim(-1,1)

plt.show()
