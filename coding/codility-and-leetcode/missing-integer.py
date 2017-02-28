# Codility. MissingInteger
def solution(A):
    occurrence = [False] * (len(A) + 1)

    for item in A:
        if 1 <= item <= len(A) + 1:
            occurrence[item-1] = True

    print(occurrence)
    for index in range(len(A) + 1):
        if occurrence[index] == False:
            return index + 1

    return -1


print(solution([1, 3, 2, 5]))
print(solution([-5, -3, -2, -1]))
print(solution([-5, -3, -2, -1, -4]))
print(solution([1, 2, 3]))
print(solution([0, 1]))
print(solution([0]))
print(solution([-2147483648, -5, 0, 2]))
print(solution([-2147483648, -5, 0, 1, 2]))
print(solution([1, 3, 6, 4, 1, 2]))
print(solution([2, 3, -156456, -1, 1, 4, 5, 150, 1050]))