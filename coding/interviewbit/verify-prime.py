# Verify Prime

def isPrime(A):
	if A < 2:
		return 0
	upperLimit = int(A**0.5)
	for i in xrange(2, upperLimit + 1):
		if i < A and A % i == 0:
			return 0
	return 1

print(isPrime(5))