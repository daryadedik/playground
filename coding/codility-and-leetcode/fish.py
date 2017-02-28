# Codility. Fish
def fish(A, B):
    for i in range(len(B) - 1):
        if B[i] == 1 and B[i+1] == 0:
            if A[i] > A[i+1]:
                A.pop(i+1)
                B.pop(i+1)
            else:
                A.pop(i)
                B.pop(i)
    return A

print(fish([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))