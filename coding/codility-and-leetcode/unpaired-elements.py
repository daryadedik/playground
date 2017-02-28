# find number of unpaired elements
def solution(S):
    D = {}
    for i, v in enumerate(S):
        D.setdefault(v, 0)
        if v in D:
            D[v] += 1

    for v in D:
        if D[v] == 1:
            return 1

    return 0

print(solution('aabbrrt'))
print(solution([1, 2, 3, 2, 3, 1, 9, 9]))

