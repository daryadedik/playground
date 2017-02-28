# Codility. Dominator
from collections import defaultdict

def solution2(A):
  d = defaultdict(int)
  b = -1

  for i in A:
    d[i] += 1

  for i in d.keys():
    if d[i] > len(A) / 2:
      b = i

  for i in range(len(A)):
    if A[i] == b:
      return i

  return b

def solution(A):
  ind = 0
  counter = 0

  for i, v in enumerate(A):
    if v == A[ind]:
      counter += 1
    elif counter > 1:
      counter -= 1
    else:
      ind = i

  counter = 0
  for v in A:
    if v == A[ind]:
      counter += 1

  return A[ind] if counter > len(A) / 2 else -1

print(solution([2, 3, 2, 4, 3, 6, 3, 3, 1]))
print(solution([2, 1, 2, 2, 8, 2, 1]))
print(solution([1, 2, 3]))
print(solution([1]))
print(solution([]))
print(solution([1, 2]))