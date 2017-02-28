# Prime Numbers

def isPrime(A):
	if A < 2:
		return 0
	upperLimit = int(A**0.5)
	for i in xrange(2, upperLimit + 1):
		if i < A and A % i == 0:
			return 0
	return 1

def sieve(A):
    primes = []
    for i in xrange(2, A + 1):
        if isPrime(i):
            primes.append(i)
    return primes

print(sieve(10))