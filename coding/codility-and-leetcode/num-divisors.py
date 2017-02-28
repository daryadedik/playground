# find the number of divisors for a given number
import math

def solution(N):
  count = 0
  for i in range(1, int(math.sqrt(N)) + 1):
    if i * i == N:
      count += 1
    elif N % i == 0:
      count += 2
  return count

print(solution(16))
print(solution(25))
print(solution(3))
print(solution(33))