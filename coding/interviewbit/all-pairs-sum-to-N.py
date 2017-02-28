def squareSum(A):
	ans = []
	a = 0
	if A == 0:
		ans.append([0, 0])
	while a * a < A:
		b = 0
		while b * b < A:
			if a * a + b * b == A and a <= b:
				newEntry = [a, b]
				ans.append(newEntry)
			b += 1
		a += 1
	return ans

print(squareSum(0))