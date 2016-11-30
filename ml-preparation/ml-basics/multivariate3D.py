# 2.1.1

import numpy as np
import matplotlib
import random
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.mlab import bivariate_normal
from mpl_toolkits.mplot3d import axes3d, Axes3D
np.random.seed(20)

num_points = 100
mean = [0, 0] #mean - 0
cov = [[10, 0], [0, 10]] #covariance matrix
points = np.random.multivariate_normal(mean, cov, size = num_points)
x, y = points.T
X, Y = np.meshgrid(x, y)

Z = bivariate_normal(X, Y)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X, Y, Z)
fig.savefig('multivariate3D.jpg')
