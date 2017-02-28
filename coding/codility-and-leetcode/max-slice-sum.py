# Codility. MaxSliceSum.
def solution(A):
    if not A:
        return 0
    if len(A) == 1:
        return A[0]

    sum_cur, max_sum = 0, -100000000

    for i in range(len(A)):
        sum_cur += A[i]
        if sum_cur > max_sum:
            max_sum = sum_cur
        if sum_cur < 0:
            sum_cur = 0
    return max_sum

print(solution([1, 2, 3, 4]))
print(solution([3, 2, -6, 4, 0, 15]))