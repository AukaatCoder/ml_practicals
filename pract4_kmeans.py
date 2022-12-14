# -*- coding: utf-8 -*-
"""pract4_kmeans

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MktfxcUcsCzSFsjM66KGn2eP4VJ4if6d
"""

import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from sklearn.cluster import KMeans
style.use('ggplot')

#ORIGINAL:

X = np.array([[1, 2],
              [1.5, 1.8],
              [5, 8],
              [8, 8],
              [1, 0.6],
              [9, 11]])

clf = KMeans(n_clusters=2)
clf.fit(X)

centroids = clf.cluster_centers_
print("cdnroids \n", centroids)
labels = clf.labels_
print("labels",labels)

colors = ["g.","r.","c.","y."]
for i in range(len(X)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)
plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)
plt.show()