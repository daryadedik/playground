import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

D = 2
K = 3
N = 100

h = 100 #fisrt hidden layer
h2 = 100 #second hidden layer

W = 0.01 * np.random.randn(D,h)
b = np.zeros((1, h))
W1 = 0.01 * np.random.randn(h,h2)
b1 = np.zeros((1, h2))
W2 = 0.01 * np.random.randn(h2,K)
b2 = np.zeros((1, K))

X = np.zeros((N*K,D))
y = np.zeros(N*K, dtype='uint8')

# initialize data
for j in range(K):
	ix = range(N*j, N*(j+1))
	r = np.linspace(0.0, 1, N)
	t = np.linspace(j*4, (j+1)*4, N) + np.random.randn(N)*0.2 #theta
	X[ix] = np.c_[r*np.sin(t), r*np.cos(t)]
	y[ix] = j

#hyperparameters
step_size = 1e-0
reg = 1e-3

# gradient descent loop
num_examples = X.shape[0]

for i in range(10000):
    hidden_layer1 = np.maximum(0, np.dot(X, W) + b)
    scores1 = np.dot(hidden_layer1, W1) + b1
    
    hidden_layer2 = np.maximum(0, np.dot(hidden_layer1, W1) + b1)
    scores = np.dot(hidden_layer2, W2) + b2
    
    #compute class probabilities
    exp_scores = np.exp(scores)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    
    #compute Loss
    correct_logprobs = -np.log(probs[range(num_examples), y])
    data_loss = np.sum(correct_logprobs)/num_examples
    reg_loss = 0.5*reg*np.sum(W*W) + 0.5*reg*np.sum(W1*W1) + 0.5*reg*np.sum(W2*W2)
    loss = data_loss + reg_loss
    
    if i % 1000 == 0:
        print "iteration %d: loss %f" % (i, loss)
        
    #compute gradient
    dscores = probs
    dscores[range(num_examples), y] -= 1 #gradient
    dscores /= num_examples
    
    #backprop into parameters W2 and b2
    dW2 = np.dot(hidden_layer2.T, dscores)
    db2 = np.sum(dscores, axis=0, keepdims=True)
    #into hidden layer
    dhidden2 = np.dot(dscores, W2.T)
    #backprop the ReLU non-linearity
    dhidden2[hidden_layer2 <= 0] = 0
    
    #backprop into parameters W1 and b1
    dW1 = np.dot(hidden_layer1.T, dhidden2)
    db1 = np.sum(dhidden2, axis=0, keepdims=True)
    #into hidden layer
    dhidden = np.dot(dhidden2, W1.T)
    #backprop the ReLU non-linearity
    dhidden[hidden_layer1 <= 0] = 0
    
    # on W,b
    dW = np.dot(X.T, dhidden)
    db = np.sum(dhidden, axis=0, keepdims=True)

    #regularization gradient contribution
    dW2 += reg*W2
    dW1 += reg*W1
    dW += reg*W
    
    #parameter update
    W += -step_size * dW
    b += -step_size * db
    W1 += -step_size * dW1
    b1 += -step_size * db1
    W2 += -step_size * dW2
    b2 += -step_size * db2

hidden_layer1 = np.maximum(0, np.dot(X, W) + b)
scores1 = np.dot(hidden_layer1, W1) + b1
hidden_layer2 = np.maximum(0, np.dot(hidden_layer1, W1) + b1)
scores = np.dot(hidden_layer2, W2) + b2
predicted_class = np.argmax(scores, axis=1)
print 'training accuracy: %.4f' % (np.mean(predicted_class == y))