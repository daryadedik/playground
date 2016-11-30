import numpy as np
import matplotlib
import random
matplotlib.use('Agg')
import matplotlib.pyplot as plt

np.random.seed(50)
d = 2
n = 10
i = 1
Ntrn = 100

mu1 = np.random.rand(d)
mu2 = np.random.rand(d)
S1 = np.random.rand(d, d)
S2 = np.random.rand(d, d)
mu1 = list(mu1 - i)
mu2 = list(mu2 + i)

def get_random_sample(n, mu1, mu2, S1, S2):

    mu_1, sigma_1 = mu1, np.dot(S1, S1.T).tolist() 
    points_1 = np.random.multivariate_normal(mu_1, sigma_1, n)
    
    mu_2, sigma_2 = mu2, np.dot(S2, S2.T).tolist()
    points_2 = np.random.multivariate_normal(mu_2, sigma_2, n)
    
    X_n = np.concatenate((points_1, points_2), axis=0)
    
    Y1 = np.ones((n,), dtype=np.int)
    Y2 = -np.ones((n,), dtype=np.int)
    
    Y_n = np.concatenate((Y1, Y2), axis=0)
    return (X_n, Y_n)

X, Y = get_random_sample(n, mu1, mu2, S1, S2)
#random.shuffle(X)

categories = np.array(Y)
colormap = np.array(['r', 'g', 'b'])

fig = plt.figure()
plt.scatter(X[:,0], X[:,1], s=50, c=colormap[categories])
fig.savefig('data_perceptron.jpg')

# Training

def perceptron(valX, valY):
    w = np.array([0, 0])
    b = 0
    
    c = list(zip(valX, valY))
    random.shuffle(c)
    valX, valY = zip(*c)
    
    for i, j in zip(valX, valY):
        prod = (np.dot(i.T, w) + b)*j
        print(j)
        print(np.dot(i.T, w) + b)
        if prod <= 0.0:
            w = w + i*j
            b = b + j
        
    return (w, b)

valw, valb = perceptron(X, Y)

def graph(formula, x_range):  
    x = np.array(x_range)  
    y = eval(formula)
    plt.plot(x, y)  
    fig.savefig('decision_boundary.jpg')

graph('valw*x + valb', range(-1, 1))