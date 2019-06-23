# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 11:08:42 2018

Week 4. Pandas. Bird Migration.

Using Datetime
    
    * timestamped data using datetime
    * how to measure elapsed time
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

birddata = pd.read_csv("./Data/bird_tracking.csv")

birddata.info()

#------------------------------------------------------------------------------
import datetime

time_1 = datetime.datetime.today()

time_2 = datetime.datetime.today()

time_2 - time_1

datetime.date.today()
datetime.datetime.now()

#------------------------------------------------------------------------------

# convert to datetime object that supports numeric operations
# add new column to the data set

birddata["date_time"].head()

timestamps = []
for k in range(len(birddata)):
    timestamps.append(datetime.strptime\
                      (birddata["date_time"].iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))

birddata["timestamps"] = pd.Series(timestamps, index = birddata.index)
birddata.head()

#------------------------------------------------------------------------------
# convert to datetime object using pandas function
birddata["timestamps"] = pd.to_datetime(birddata["date_time"])
birddata.head()

# elapsed time
times = birddata["timestamps"][birddata["bird_name"] == "Eric"]
elapsed_time = times - times[0]

#------------------------------------------------------------------------------
