# Codility. Ladder. Complexity is O(N) overall. 62%

def fibonacci(N):
  if N < 1:
    return 0

  fib = [0] * (N + 1)
  fib[1] = 1
  for i in range(2, len(fib)):
    fib[i] = fib[i-1] + fib[i-2]
  return fib[N]

def ladder(A, B):
    sequence = []
    for i, v in enumerate(A):
        sequence.append(fibonacci(v+1))

    for i, v in enumerate(B):
        sequence[i] = sequence[i] % (2 ** v)

    return sequence

print(ladder([4, 4, 5, 5, 1], [3, 2, 4, 3, 1]))