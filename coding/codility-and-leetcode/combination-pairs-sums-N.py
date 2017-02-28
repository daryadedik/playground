# Find number of pairs that sums to N
def solution(A, N):
    count = 0

    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] + A[j] == N:
                count += 1
    return count


print(solution([2, 4, 2, 0, 0], 5))
print(solution([2, 4, 2, 1, 0], 5))
print(solution([5], 5))
print(solution([], 5))