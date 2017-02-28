# Codility. PermMissingElem.
def missingElement(arr):
    N = len(arr)
    expected_sum = (N + 1) * (N + 2) / 2
    current_sum = 0

    for i in range(N):
        current_sum = current_sum + arr[i]

    return expected_sum - current_sum

print(missingElement([1, 2, 4, 5]))
print(missingElement([]))
print(missingElement([1, 2, 3, 4]))
