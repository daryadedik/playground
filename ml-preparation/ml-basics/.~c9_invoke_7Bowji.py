# 2.1.1

import numpy as np
import matplotlib
import random
matplotlib.use('Agg')
import matplotlib.pyplot as plt
np.random.seed(2)

num_points = 100

fig = plt.figure()
mean = [0, 0] #mean - 0
cov = [[1, 0], [0, 1]] #covariance matrix
points = np.random.multivariate_normal(mean, cov, size=num_points)
x, y = points.T
plt.plot(x, y, 'ro')
fig.savefig('multivariate2D.jpg')

# 2.1.2
corr_coef = np.corrcoef(x, y)
print ("Correlation coefficients: \n {}".format(corr_coef))

# 2.1.3
mu = np.random.rand(2, num_points) # 2x100
A = np.random.rand(2, 2) # 2x2
Z = mu + np.dot(A, points.T) # 2x100

x_z, y_z = Z #new points
plt.plot(x_z, y_z, 'ro')
fig.savefig('multivariate2D_2.jpg')
corr_coef = np.corrcoef(x_z, y_z)
print "\n Correlation coefficients: \n {}".format(corr_coef)

# 2.1.4
X_cov = np.cov(x, y)
print "\n Covariance matrix for X: \n {}".format(X_cov)
Z_cov = np.cov(x_z, y_z)
print "\n Covariance matrix for Z: \n {}".format(Z_cov)

B = np.dot(A, A.T) # B = A * A'
dist = np.linalg.norm(Z_cov-B)
print "\n Distance between Z_cov and B: {}".format(dist)