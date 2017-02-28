# Standard binary search.
def solution(A, N):
  begin, end = 0, len(A) - 1

  while begin <= end:
    mid = (begin + end) / 2
    if N > A[mid]:
      begin = mid + 1
    elif N == A[mid]:
      return mid
    else:
      end = mid - 1

  return -1

print(solution([-1, 3, 5, 6, 9, 15], 9))
print(solution([], 9))
print(solution([1, 2], 2))
print(solution([2], 9))
print(solution([2], 2))