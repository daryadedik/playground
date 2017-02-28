# MaxProfit. Codility
import sys

def solution(A):
    min_price = sys.maxint
    max_profit = 0
    for a in A:
        min_price = min(a, min_price)
        max_profit = max(a - min_price, max_profit)
    return max_profit

def solution_incorrect(A):
    min_el = sys.maxint
    max_el = 0
    ind = 0
    for i, v in enumerate(A):
        if v < min_el:
            min_el = v
            ind = i

    for i in range(ind, len(A)):
        if A[i] > max_el:
    	    max_el = A[i]

    return max_el - min_el if max_el - min_el > 0 else 0


print(solution([23171, 21011, 21123, 21366, 21013, 21367]))
print(solution([23171, 21045, 21123, 21366, 21013, 21212]))
print(solution([45, 55]))
print(solution([55, 45]))
print(solution([0, 25, 23, 0, 78]))
print(solution([]))