# Codility. Distinct
def distinct(A):
    n = len(A)
    if n == 0:
        return 0

    A.sort()

    unique = 1
    for i in range(1, n):
        if A[i] != A[i - 1]:
            unique += 1
    return unique

print(distinct([1, 5, 3, 7, 2, 5, 9]))
print(distinct([]))
print(distinct([1, 1, 1, 1]))
print(distinct([-190, -1798, -15653, 0, 0, -190]))