# Find Nth fibonacci number
def fibonacci_recursive(n):
  if (n <= 1):
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci(N):
  if N < 1:
    return 0

  fib = [0] * (N + 1)
  fib[1] = 1
  for i in range(2, len(fib)):
    fib[i] = fib[i-1] + fib[i-2]
  return fib[N]

print(fibonacci(5))
print(fibonacci(0))
print(fibonacci(11))