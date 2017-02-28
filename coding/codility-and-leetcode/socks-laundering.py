# Codility. SocksLaundering. 80%
from collections import Counter, defaultdict

def solution(K, C, D):
  clean = Counter(C)
  dirty = Counter(D)

  num_pairs = 0

  for k, v in clean.items():
    if k in dirty and v % 2 != 0 and K > 1:
      clean[k] += 1
      dirty[k] -= 1
      num_pairs += clean[k] // 2
      K -= 1
      if dirty[k] == 0:
        del dirty[k]
    else:
      num_pairs += v // 2

  for _, v in dirty.items():
    if v != 1 and K > 0 and K != 1:
      if v <= K:
        num_pairs += v // 2
        K -= v
      else:
        num_pairs += K // 2
        K -= K // 2

  return num_pairs

print(solution(4, [1, 2, 2, 2, 5], [5, 5, 1, 1, 2]))
print(solution(4, [1, 2, 1, 1], [1, 4, 2, 3, 4]))
print(solution(2, [1, 2, 1, 1], [1, 4, 2, 3, 4]))
print(solution(2, [1], [3]))
print(solution(12, [1, 3], [1, 3]))
print(solution(7, [1, 2, 3, 4, 5, 6, 3, 2, 4, 7], [2, 7, 4, 3, 2]))
print(solution(2, [2, 2, 3, 3, 4, 2, 4], [2, 2, 2, 3, 3, 3, 3, 4, 4]))
print(solution(3, [1, 2], [8, 8, 8, 8, 9]))
print(solution(0, [1, 2], [8, 8, 8, 8, 9]))
print(solution(2, [1, 2], []))
print(solution(2, [], [1, 1]))
print(solution(2, [], [1, 2]))
print(solution(0, [], []))
print(solution(5, [1, 1, 3, 4], [3, 3, 3, 5]))
print(solution(0, [1, 2, 3, 4], [3, 2, 1, 5]))

#https://codility.com/demo/results/trainingWRPMU9-2FN/