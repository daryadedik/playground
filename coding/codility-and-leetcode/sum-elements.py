# Number of pairs sums to N
from collections import defaultdict

def solution(A, N):
  count = 0

  D = defaultdict(int)
  for v in A:
    D[N-v] += 1

  for v in A:
    if v in D:
      count += D[v]

  return count / 2

print(solution([3, 7, 9, 2, 3, 2, 4, 1], 5))
print(solution([3, 7, 9, 2, 4, 1], 5))
print(solution([1, 2, 3, 4, 5, 6, 7, 8], 9))
print(solution([1, 3, 6, 6, 8, 2, 0], 77))