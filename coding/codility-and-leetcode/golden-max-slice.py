# Find sum of elements which form maximum slice (biggest sum)
#O(n)
def golden_max_slice(A):
  max_ending = max_slice = 0
  for a in A:
    max_ending = max(0, max_ending + a)
    max_slice = max(max_slice, max_ending)
  return max_slice

#O(n^2)
def solution(A):
  n = len(A)
  result = 0
  for p in range(n):
    sum = 0
    for q in range(p, n):
      sum += A[q]
      print(sum)
      result = max(result, sum)
  return result

#O(n^3)
def solution2(A):
  max_sum = 0
  for i in range(len(A)):
    for j in range(i, len(A)):
      sum = 0
      for k in range(i, j + 1):
        sum += A[k]
      max_sum = max(max_sum, sum)
  return max_sum

#print(solution([2, 4, 1, -5, 5, 7, 2]))
#print(golden_max_slice([5, -7, 3, 5, -2, 4, -1]))
print(golden_max_slice([3, 2, -6, 4, 0, 10]))
print(golden_max_slice([2, 40]))
print(golden_max_slice([2, -10]))
print(golden_max_slice([4, -5, 3, 9]))