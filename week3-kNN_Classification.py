# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 12:05:14 2018

@author: Olena

Week 3 Intro to Classification
kNN classification

"""
import numpy as np

def distance(p1, p2):
    
    """ Find the distance between points p1 and p2.  """
    
    return np.sqrt(np.sum(np.power(p2-p1, 2)))

#------------------------------------------------------------------------------

import random

def majority_vote(votes):
    """
    Return most frequent element in a sequence
    If some elements have the same frequence, pick up one randomly
    """
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1
            
    winners = []
    max_count = max(vote_counts.values())
    
    for vote, count in vote_counts.items():
        if count == max_count:
            winners.append(vote)
                 
    return random.choice(winners)

#------------------------------------------------------------------------------

votes = [1,2,3,1,2,3,3,3,3,3, 2,2,2, 2]
majority_vote(votes)

"""
Most frequently element in a sequence is called mode in statistics

"""
import scipy.stats as ss

def majority_vote_short(votes):
    """
    Return the most common element in a sequence
    
    """
    mode, count = ss.mstats.mode(votes)          
           
    return mode

majority_vote_short(votes)

#-----------------------------------------------------------------------------

def find_neares_neighbors(p, points, k=5):
    
    """ Find the k nearest neighbors of point p and return their indicies """
    
    distances = np.zeros(points.shape[0])
    
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    
    # return indecies of sorted elemenets
    ind = np.argsort(distances)
    
    return ind[0:k]

#------------------------------------------------------------------------------
    
def knn_predict(p, points, outcomes, k = 5):
    """ 
    Return class label of point `p` based on classes of `k` nearest neghbors 
    `p` is a new point which class we would like to define
    `outcomes` is an array of labels of `points` """
    
    ind = find_neares_neighbors(p, points, k)
    return majority_vote(outcomes[ind])
    
#------------------------------------------------------------------------------    
# test data

import matplotlib.pyplot as plt

points = np.array([[1,1], [1,2], [1,3], [2,1], [2,2], [2,3], [3,1], [3,2], [3,3]])
p = np.array([2.5, 2.7])

outcomes = np.array([0,0,0,0,1,1,1,1,1])

plt.plot(points[[outcomes == 0]][:, 0], points[[outcomes == 0]][:, 1],  "ro")
plt.plot(points[[outcomes == 1]][:, 0], points[[outcomes == 1]][:, 1], "go")
plt.plot(p[0], p[1], "bo")

knn_predict(p, points, outcomes, k = 2)

#------------------------------------------------------------------------------
# generating sythetic data
def generate_synth_data(n = 50):
    """ Generating sythetic data 
    Create two sets of points from bivariate normal distribution """
    
    points = np.concatenate((ss.norm(0,1).rvs((n,2)), ss.norm(1,1).rvs((n,2))), axis = 0)
    outcomes = np.concatenate((np.repeat(0,n), np.repeat(1,n)) )
    
    return (points, outcomes)

n = 20
points, outcomes = generate_synth_data(n)

plt.figure()
plt.plot(points[:n, 0], points[:n, 1], "ro")
plt.plot(points[n:, 0], points[n:, 1], "bo")

#------------------------------------------------------------------------------

def make_prediction_grid(predictors, outcomes, limits, h, k):
    """ Classify each point in prediction grid."""
    
    (x_min, x_max, y_min, y_max) = limits
    xs = np.arange(x_min, x_max, h)
    ys = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs, ys)
    
    prediction_grid = np.zeros(xx.shape, dtype = int)
    
    for i, x in enumerate(xs):
        for j, y in enumerate(ys):
            p = np.array([x,y])
            prediction_grid[j,i] = knn_predict(p, predictors, outcomes, k)
    
    return (xx, yy, prediction_grid)
    
#------------------------------------------------------------------------------
def plot_prediction_grid (xx, yy, prediction_grid, filename):
    """ Plot KNN predictions for every point on the grid."""
    from matplotlib.colors import ListedColormap
    background_colormap = ListedColormap (["hotpink","lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap (["red","blue","green"])
    plt.figure(figsize =(10,10))
    plt.pcolormesh(xx, yy, prediction_grid, cmap = background_colormap, alpha = 0.5)
    plt.scatter(predictors[:,0], predictors [:,1], c = outcomes, cmap = observation_colormap, s = 50)
    plt.xlabel('Variable 1'); plt.ylabel('Variable 2')
    plt.xticks(()); plt.yticks(())
    plt.xlim (np.min(xx), np.max(xx))
    plt.ylim (np.min(yy), np.max(yy))
    plt.savefig(filename)    

#------------------------------------------------------------------------------

predictors, outcomes =  generate_synth_data()
k = 5; filename = "./Figs/knn_synth_5.pdf"; limits = (-3,4,-3,4); h = 0.1 
(xx, yy, prediction_grid) = make_prediction_grid(predictors, outcomes, limits, h, k)
plot_prediction_grid (xx, yy, prediction_grid, filename)

#------------------------------------------------------------------------------

from sklearn import datasets
iris = datasets.load_iris()

predictors = iris.data[:, 0:2]
outcomes = iris.target
plt.plot(predictors[outcomes == 0][:, 0], predictors[outcomes == 0][:, 1], "ro")
plt.plot(predictors[outcomes == 1][:, 0], predictors[outcomes == 1][:, 1], "go")
plt.plot(predictors[outcomes == 2][:, 0], predictors[outcomes == 2][:, 1], "bo")

plt.savefig("./Figs/iris.pdf")

k = 5; filename = "./Figs/iris_grid.pdf"; limits = (-4, 8, 1.5, 4.5); h = 0.1 
(xx, yy, prediction_grid) = make_prediction_grid(predictors, outcomes, limits, h, k)
plot_prediction_grid (xx, yy, prediction_grid, filename)

#------------------------------------------------------------------------------

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(predictors, outcomes)
sk_predictions = knn.predict(predictors)

my_predictions = np.array([knn_predict(p, predictors, outcomes, k=5) for p in predictors])

np.mean(sk_predictions == outcomes)
np.mean(my_predictions == outcomes)

