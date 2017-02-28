# Codility. FrogRiverOne
def solution(X, A):
    time = [-1] * X
    leaves = X

    for i in range(len(A)):
        if A[i] > X or time[A[i]-1] != -1:
            continue
        else:
            time[A[i]-1] = i
            leaves -= 1
            if leaves == 0:
                return i
    return -1

# O(n^2)
def solution2(X, A):
    fallen = []
    ind = 0
    for i in range(len(A)):
        if A[i] not in fallen and A[i] <= X:
            fallen.append(A[i])
            ind = i

    return ind if len(fallen) == X else -1

print(solution(5, [1, 2, 3, 5, 4]))
print(solution(3, [1, 2, 5, 6, 7]))
print(solution(3, [1, 2, 3]))
print(solution(3, [2, 3]))
print(solution(3, [1]))