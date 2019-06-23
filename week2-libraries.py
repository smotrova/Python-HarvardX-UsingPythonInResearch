# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 14:29:33 2018

Python for Research

Week 2

Libraries and Concepts

"""

# numpy basics

import numpy as np

dir(np)

np.arange(1,100)
np.linspace(1, 100, 10)

np.logspace(1, 2, 10)

type(np.random.random(10))
np.size(np.random.random(10))

# matplotlib basics

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,20)
y1 = x**2.0
y2 = x**1.5

fig = plt.figure()
type(fig)

ax = fig.add_subplot(111)
type(ax)

ax.plot(x, y1, "ro-")
ax.plot(x, y2, "gs")
plt.show()


