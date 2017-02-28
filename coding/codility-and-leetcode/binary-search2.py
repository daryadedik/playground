# Binary search
def binary_search(n, List):
    bottom = 0
    top = len(List) - 1

    Found = False
    while not Found and bottom <= top:
        middle = (bottom + top) // 2
        if List[middle] == n:
            Found = True
        elif List[middle] < n:
            bottom = middle + 1
        else:
            top = middle - 1
    return Found

print(binary_search(12, [1,5,7,8,9,15,18,25]))