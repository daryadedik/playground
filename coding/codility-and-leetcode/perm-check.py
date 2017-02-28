# Codility. PermCheck
def perm_check(arr):
    bitmap = [False] * len(arr)

    for i in arr:
        if 1 <= i <= len(arr) and not bitmap[i - 1]:
            bitmap[i - 1] = True
        else:
            return 0

    return 1 if all(bitmap) else 0

print(perm_check([1, 4, 3, 2]))
print(perm_check([]))
print(perm_check([1, 2, 2, 7, 4]))
print(perm_check([1, 2, 2, 3, 4]))
print(perm_check([1, 2, 3, 4, 5, 6]))
print(perm_check([1]))
print(perm_check([0]))
print(perm_check([1, 4]))