def solution(A, B, C):
    total, front, num_int = 0, 0, 0

    for back in xrange(len(A)):
        while front < len(A) and A[front] + total <= C:
            total += A[front]
            front += 1
            if B <= total <= C:
                num_int += 1
        total -= A[back]
    return num_int


def solution1(A, B, C):
    i = 0
    j = 0
    n_int = 0
    cur_sum = 0
    while j < len(A):
        if i != j and B <= cur_sum + A[j] <= C:
            n_int += 1
            cur_sum += A[i] + A[j]
            j += 1
        elif i == j:
            if B <= A[i] <= C:
                n_int += 1
            elif A[i] <= C:
                cur_sum = A[i]
            j += 1
        else:
            i += 1
            cur_sum -= A[i]

    return n_int


def solution2(A, B, C):
    l = list()
    for i in xrange(len(A)):
        for j in xrange(i, len(A)):
            if sum(A[i:j+1]) >= B and sum(A[i:j+1]) <= C:
                l.append(A[i:j+1])
    return len(l)

#print(solution([10, 5, 1, 0, 2], 6, 8))
#print(solution([6, 9, 5, 3], 5, 8))
print(solution([3, 7, 6, 2, 1], 6, 8))
#print(solution([ 76, 22, 81, 77, 95, 23, 27, 35, 24, 38, 15, 90, 19, 46, 53, 6,
#77, 96, 100, 85, 43, 16, 73, 18, 7, 66 ], 98, 290))
print(solution([ 80, 97, 78, 45, 23, 38, 38, 93, 83, 16, 91, 69, 18, 82, 60, 50, 61, 70, 15, 6, 52, 90], 99, 269))