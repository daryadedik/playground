# Codility. MinMaxDivision
def find_max_sum(K, A, S):
    cur_sum = 0
    max_sum = 0

    for i in A:
        cur_sum += i
        if K > 1 and cur_sum > S:
            max_sum = max(max_sum, cur_sum - i)
            cur_sum = i
            K -= 1
    return max(max_sum, cur_sum)

def solution(K, M, A):
    end = M * len(A)
    beg = 0
    min_sum = M * len(A)

    while beg <= end:
        mid = (beg + end) / 2
        max_sum = find_max_sum(K, A, mid)
        if max_sum > mid:
            beg = mid + 1
        elif max_sum == mid:
            min_sum = min(min_sum, max_sum)
            end = mid - 1
        else:
            end = mid - 1

    return min_sum
