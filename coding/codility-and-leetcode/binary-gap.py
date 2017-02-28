# Codility. BinaryGap
def binary_gap(N):
    maximum_gap = 0
    curr_gap = 0

    # Skip zeros in the beginning of a binary representation of N
    while N > 0 and N % 2 == 0:
        N //= 2

    if N == 1:
        return 0

    while N > 0:
        rem = N % 2
        print(rem)
        if rem == 0:
            curr_gap += 1
        else:
            if curr_gap != 0:
                maximum_gap = max(curr_gap, maximum_gap)
                curr_gap = 0
        N //= 2

    return maximum_gap

Num = 35
print("Binary representation of {} is {}".format(Num,  "{0:b}".format(Num)))
print("Binary gap length: {}".format(binary_gap(Num)))