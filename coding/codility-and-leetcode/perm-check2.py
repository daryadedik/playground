# Codility. PermCheck. Other variants.
def hashmap(arr):
    arr_unique = {}

    for i in arr:
        if i in arr_unique:
            arr_unique[i] += 1
        else:
            arr_unique[i] = 1
    return arr_unique


def perm_check(arr):
    if len(arr) == 0 or any(t == 0 for t in arr):
        return 0
    unique_vals = hashmap(arr)
    max_key = max(unique_vals.keys())
    if len(unique_vals) != max_key or any(t != 1 for t in unique_vals.values()):
        return 0
    else:
        return 1

print(perm_check([4, 1, 3, 5, 6, 8, 7, 7]))
print(perm_check([1, 2, 3]))
print(perm_check([0]))
print(perm_check([]))
print(perm_check([1, 4]))