# Codility demo test
def grocery_store(A):
    n = len(A)
    size, result = 0, 0
    for i in xrange(n):
        if A[i] == 0:
            size += 1
        else:
            size -= 1

    return max(result, -size)

print(grocery_store([0, 1, 1, 1]))