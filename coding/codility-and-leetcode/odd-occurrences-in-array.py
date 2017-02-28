# Codility. OddOccurrencesInArray
arr = [0, 0, 1]

def OddOccurrencesInArray(A):
    if len(A) % 2 is 0 or any(x == 0 for x in A):
        return 0
    elif len(A) < 2:
        return A[0]
    else:
        xor = A[0] ^ A[1]
        for i in range(1, len(A) - 1):
            xor = xor ^ A[i + 1]
    return xor

print(OddOccurrencesInArray(arr))
print(OddOccurrencesInArray([1, 2, 4, 5, 4, 5, 1, 9]))