# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 09:12:13 2018

@author: Olena

Week 3 Case study 3

Wine classification with kNN

"""

import numpy as np
import pandas as pd
# pd.__version__
import matplotlib as plt
import scipy.stats as ss
import random

from sklearn.neighbors import KNeighborsClassifier

#------------------------------------------------------------------------------
""" Read in the data as a `pandas` dataframe using `pd.read_csv`. """

data = pd.read_csv("./Data/wine.csv")

data.info()
data.head()
data.describe()

data.index
data.columns

data["color"].value_counts()

