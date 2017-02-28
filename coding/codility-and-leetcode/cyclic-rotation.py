# Codility. CyclicRotation
A = [3, 8, 9, 7, 6]
k = 3

def CyclicRotation(arr, K):
    if len(A) == 0:
        return A

    remainder = K % len(A)
    if remainder == 0:
        return A
    else:
        left_sublist = A[-remainder:]
        right_sublist = A[:len(A)-remainder]
        return left_sublist + right_sublist

print(CyclicRotation(A, k))