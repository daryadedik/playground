# Count number of pairs that sums to N
from collections import defaultdict

def solution(A, N):
  count = 0

  D = defaultdict(int)
  for v in A:
    D[N-v] += 1
  print(D)

  for v in D.keys():
    if v in A:
      count += D[v]

  return count

print(solution([3, 7, 9, 2, 3], 5))
print(solution([3, 7, 9, 2, 3, 2, 4, 1], 5))
print(solution([7, 9], 5))