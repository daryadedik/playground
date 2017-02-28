# Compute decimal zip of two numbers
import itertools

def solution(A, B):
    """
    Computes the decimal zip of A and B
    """

    # only defined for non-negative integers
    if A < 0 or B < 0:
        return -1

    A_str = str(A)
    B_str = str(B)

    N = min(len(A_str), len(B_str))

    # zip A and B (up to N elements)
    zipped_str = zip(A_str, B_str)
    print list(itertools.chain(*zipped_str))
    # flatten tuples of digits into a list
    zipped = list(itertools.chain(*zipped_str))

    # append the remaining digits
    if len(A_str) > N:
        zipped.extend(A_str[N:])
    elif len(B_str) > N:
        zipped.extend(B_str[N:])

    if len(zipped) > 9:
        return -1

    # convert to int (handles the leading zero digit)
    C = int(''.join(zipped))
    if C > 100000000:
        return -1

    return C

print(445232 == solution(45, 4232))
print(10234 == solution(1234, 0))
print(1526 == solution(12, 56))
print(5162 == solution(56, 12))
print(16273845 == solution(12345, 678))
print(16273890 == solution(123, 67890))
print(11020300 == solution(10000, 123))
print(11020345 == solution(100, 12345))
print(12000000 == solution(100, 20000))
print(12000000 == solution(10000, 200))
print(-1 == solution(1000, 10000))