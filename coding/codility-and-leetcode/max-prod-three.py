# Codility. MaxProductOfThree. Find maximum product of three elements
def max_prod_three(A):
    if len(A) < 3:
        return 0
    A.sort()
    return max(A[-1]*A[-2]*A[-3], A[0]*A[1]*A[-1])

print(max_prod_three([3, -3, 5])) #-45
print(max_prod_three([0])) #0
print(max_prod_three([])) #0
print(max_prod_three([1, 2, 3, 1, 1, 1, 2]))  #12
print(max_prod_three([-2, -1, 0, 3, -1, -2])) #12
print(max_prod_three([1, 2])) #0
print(max_prod_three([3, 2, -3, -1, -7])) #63
print(max_prod_three([1, 10, -5, 1, -100])) #63