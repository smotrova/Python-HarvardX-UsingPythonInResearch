# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 16:39:00 2018

@author: Olena

Random Walker
"""

import numpy as np
import matplotlib.pyplot as plt

X_0 = np.array([[0], [0]]) 
deltaX = np.random.normal(0, 1, (2,10) )
X = np.concatenate((X_0, np.cumsum(deltaX, axis = 1)), axis = 1)

plt.plot(X[0], X[1], "ro-")
plt.xlabel("$X$")
plt.ylabel("$Y$")
plt.title("Random Walker");


z = X[:, 0].copy()