
"""
Created on Mon Nov 19 12:53:23 2018

@author: Olena

Week 4. Pandas. Classification

case studies: whisky classification

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster.bicluster import SpectralCoclustering

whisky = pd.read_csv("./Data/whiskies.txt")
whisky["Region"] = pd.read_csv("./Data/regions.txt")

whisky.info()

whisky.head()

whisky.iloc[0:3]
whisky.loc[0:3]

whisky.columns

flavors = whisky.iloc[:, 2:14]

# correlation
corr_flavors = pd.DataFrame.corr(flavors)

plt.figure(figsize = (10,10))
plt.pcolor(corr_flavors)
plt.colorbar()
plt.savefig("./Figs/Flavor-corr.pdf")

corr_whiskey = pd.DataFrame.corr(flavors.transpose())
plt.figure(figsize = (10,10))
plt.pcolor(corr_whiskey)
plt.colorbar()
plt.savefig("./Figs/Whiskey-corr.pdf")


# Clustering Whiskies By Flavor Profile

model = SpectralCoclustering(n_clusters = 6, random_state = 0)
model.fit(corr_whiskey)

model.rows_

# how many observations in each clusters
np.sum(model.rows_, axis = 1)

model.row_labels_
# interpretation: observation number 0 belongs to cluster number 5, obs 1 to cl 2 ...

whisky["Group"] = pd.Series(model.row_labels_, index = whisky.index)
whisky = whisky.ix[np.argsort(model.row_labels_)]
whisky = whisky.reset_index(drop = True)

correlations = pd.DataFrame.corr(whisky.iloc[:, 2:14].transpose())
correlations = np.array(correlations)

plt.figure(figsize = (10,10))
plt.pcolor(correlations)
plt.colorbar()
plt.savefig("./Figs/correlations.pdf")

