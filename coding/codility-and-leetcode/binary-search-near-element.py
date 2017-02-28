# Find closes element to n with binary search
def binary_search(n, List):
    bottom = 0
    top = len(List) - 1

    Found = False
    while not Found and bottom <= top:
        middle = (bottom + top) // 2
        if List[middle] == n:
            Found = True
            return List[middle]
        elif List[middle] < n:
            bottom = middle + 1
        else:
            top = middle - 1
    return List[middle]

print(binary_search(6, [1,1,5,10]))