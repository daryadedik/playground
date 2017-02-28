# Codility. CountDistinctSlices
def solution(M, A):
    B = [False] * (M + 1)
    count, front = 0, 0
    ub = 1000000000

    for back, v in enumerate(A):
        if not B[A[front]]:
            num = front - back
            count -= num * (num + 1) / 2
        extended = False
        while front < len(A) and not B[A[front]]:
            B[A[front]] = True
            extended = True
            front += 1
        if extended:
            num = front - back
            count += num * (num + 1) / 2
            if count > ub:
                return ub
        if front >= len(A):
            break
        B[v] = False

    return count