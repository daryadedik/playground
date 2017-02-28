# All Factors

def allFactors(A):
    import math
    factors = []
    for i in range(1, int(math.sqrt(A)) + 1):
        if i * i == A:
            factors.append(i)
        elif A % i == 0:
            factors.append(A // i)
            factors.append(i)
    factors.sort()
    return factors

print(allFactors(15))