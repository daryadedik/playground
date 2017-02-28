# Square Root Of Integer

def solution(N):
    begin, end = 0, N
    sqrt = 0

    while begin <= end:
        mid = (begin + end) / 2
        if mid * mid == N:
            return mid
        elif mid * mid > N:
            end = mid -1
        else:
            begin = mid + 1
            sqrt = mid

    return sqrt

print(solution(25))
print(solution(11))
print(solution(22))
print(solution(43))
print(solution(1))
print(solution(0))
print(solution(2))