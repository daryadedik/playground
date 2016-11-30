import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# initialize parameters randomly
N = 100 #points per class
D = 2 #dimensionality
K = 3 #number of classes
X = np.zeros((N*K,D))
y = np.zeros(N*K, dtype='uint8')

# initialize data
for j in range(K):
	ix = range(N*j, N*(j+1))
	r = np.linspace(0.0, 1, N)
	t = np.linspace(j*4, (j+1)*4, N) + np.random.randn(N)*0.2 #theta
	X[ix] = np.c_[r*np.sin(t), r*np.cos(t)]
	y[ix] = j


W = 0.01 * np.random.randn(D,K)
b = np.zeros((1, K))

#hyperparameters
step_size = 1e-0
reg = 1e-3

#gradient descent loop
num_examples = X.shape[0]
print(num_examples)
for i in range(300):
    
    #evaluate class scores
    scores = np.dot(X,W) + b
    
    #compute class probabilities
    exp_scores = np.exp(scores)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    
    #compute Loss
    correct_logprobs = -np.log(probs[range(num_examples), y])
    data_loss = np.sum(correct_logprobs)/num_examples
    reg_loss = 0.5*reg*np.sum(W*W)
    loss = data_loss + reg_loss
    
    if i % 10 == 0:
        print "iteration %d: loss %f" % (i, loss)
    
    #compute gradient
    dscores = probs
    dscores[range(num_examples), y] -= 1 #gradient
    dscores /= num_examples
    
    #backprop
    dW = np.dot(X.T, dscores)
    db = np.sum(dscores, axis=0, keepdims=True)
    
    #regularization gradient
    dW += reg*W
    
    #parameter update
    W += -step_size * dW
    b += -step_size * db
    
scores = np.dot(X,W) + b
predicted_class = np.argmax(scores, axis=1)
print 'training accuracy: %.2f' % (np.mean(predicted_class == y))