import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

N = 100 #points per class
D = 2 #dimensionality
K = 3 #number of classes

X = np.zeros((N*K,D))
y = np.zeros(N*K, dtype='uint8')

for j in range(K):
	ix = range(N*j, N*(j+1))
	#print(ix)
	r = np.linspace(0.0, 1, N)
	#print(r)
	t = np.linspace(j*4, (j+1)*4, N) + np.random.randn(N)*0.2 #theta
	#print(t.shape)
	X[ix] = np.c_[r*np.sin(t), r*np.cos(t)]
	y[ix] = j
	
num_examples = X.shape[0]
fig, ax = plt.subplots(1,1)
ax.scatter(X[:, 0], X[:,1], c=y, s=40, cmap=plt.cm.Spectral)
plt.xlim(-1, 1)
plt.ylim(-1, 1)
fig.savefig('display.png')

#training softmax
reg = 1
step_size = 0.1
W = 0.01 * np.random.randn(D,K)
b = np.zeros((1, K))
scores = np.dot(X, W) + b
#print(scores.shape)

#compute Softmax Loss
exp_scores = np.exp(scores)
probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
correct_logprobs = -np.log(probs[range(num_examples), y])
data_loss = np.sum(correct_logprobs)/num_examples
reg_loss = 0.5*reg*np.sum(W*W)
loss = data_loss + reg_loss

dscores = probs
dscores[range(num_examples), y] -= 1 #gradient
dscores /= num_examples
#print(dscores)

#backprop
dW = np.dot(X.T, dscores)
db = np.sum(dscores, axis=0, keepdims=True)
dW += reg*W

#parameter update
W += -step_size * dW
b += -step_size * db

h = 100
h2 = 100
W = 0.01 * np.random.randn(D,h)
b = np.zeros((1, h))
print(W.shape, b.shape)
W1 = 0.01 * np.random.randn(h,h2)
b1 = np.zeros((1, h2))
print(W1.shape, b1.shape)
W2 = 0.01 * np.random.randn(h2,K)
b2 = np.zeros((1, K))
print(W2.shape, b2.shape)


hidden_layer1 = np.maximum(0, np.dot(X, W) + b)
print(hidden_layer1.shape)
scores1 = np.dot(hidden_layer1, W1) + b1
print(scores1.shape)

hidden_layer2 = np.maximum(0, np.dot(hidden_layer1, W1) + b1)
print(hidden_layer2.shape)
scores2 = np.dot(hidden_layer2, W2) + b2
print(scores2.shape)

dW2 = np.dot(hidden_layer2.T, dscores)
print(dW2)