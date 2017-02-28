# Compute the number of elevator stops
def solution(A, B, M, X, Y):
    """
    Computes the number of elevator stops
    """
    N = len(A) # the number of people
    i, cnt = 0, 0

    while i < N:
        # weight - the weight of people in the elevator
        # j - the first person in the next batch
        weight, j = 0, i
        while j < N and weight + A[j] <= Y and j - i + 1 <= X:
            weight += A[j]
            j += 1
        # set() computes the unique floors plus the one stop to go down
        cnt += len(set(B[i:j])) + 1
        # start the next batch
        i = j
    return cnt

print solution([60, 70, 40], [2, 5, 4], 5, 2, 80) #3