# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 09:37:44 2018

Week 4. Pandas. Bird Migration.

    * Data Visualization
    * Datetime objects
    * Cartopy Library
    * Cartographic Projection
    
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

birddata = pd.read_csv("./Data/bird_tracking.csv")

birddata.info()
birddata.head()

birddata.columns

birddata["bird_name"].value_counts()
birddata["bird_name"].unique()


ix = birddata["bird_name"] == "Eric"
ix.value_counts()

# trajectories for each bird

bird_names = birddata["bird_name"].unique()

plt.figure()

for bird_name in bird_names:
    ix = birddata["bird_name"] == bird_name

    x, y = birddata["longitude"][ix], birddata["latitude"][ix]
    plt.plot(x,y, ".", label = bird_name)

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc = "lower right")  

plt.savefig("./Figs/3traj.pdf")  

#------------------------------------------------------------------------------
# speed

ix = birddata["bird_name"] == "Eric"
speed = birddata["speed_2d"][ix]

# NA treatment
# if are there NAs: 
np.isnan(speed).any()

# how many NAs
np.isnan(speed).value_counts()

# find NAs in array
ind = np.isnan(speed)
plt.hist(speed[~ind], ec = "black", bins = np.linspace(0, 25, 26), normed = True)
plt.xlabel("2D speed (m/s)")
plt.ylabel("Frequency");

#------------------------------------------------------------------------------
# plot histogramm using Pandas
birddata["speed_2d"][ix].plot.hist(range = [0,30], alpha = 0.7, ec="black")
plt.xlabel("2D speed (m/s)")

#------------------------------------------------------------------------------

