# Codility. EquiLeader
def solution(A):
  # find leader as in dominator.py
  ind = 0
  counter = 0

  if not A:
    return 0

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

  leader = A[ind]

  num_leader = 0
  for i, v in enumerate(A):
    if v == leader:
      num_leader += 1

  count = 0
  equi_leaders = 0
  for i, v in enumerate(A):
    if v == leader:
      count += 1
    if count > (i + 1) / 2 and num_leader - count > (len(A) - 1 - i) / 2:
       equi_leaders += 1

  return equi_leaders

print(solution([3, 4, 4, 4, 2, 4])) #2 (3, 4, 4)(4, 2, 4) and (3, 4, 4, 4, 2)(4)
print(solution([1, 6, 6, 3, 2, 6, 6, 6])) #2 (1, 6, 6)(3, 2, 6, 6, 6) and (1, 6, 6, 3, 2, 6, 6)(6)
print(solution([7, 7, 7, 7, 7])) #4 (7)(7, 7, 7, 7) and (7, 7)(7, 7, 7) and (7, 7, 7)(7, 7) and (7, 7, 7, 7)(7)
print(solution([1, 2, 3, 4, 5])) #0
print(solution([2, 3, 2, 2, 3, 2])) #0 (2)(3, 2, 2, 3, 2) and (2, 3, 2)(2, 3, 2) and (2, 3, 2, 2, 3)(2)
print(solution([]))
print(solution([1]))
print(solution([1, 2]))
print(solution([1, 2, 1, 2, 2]))