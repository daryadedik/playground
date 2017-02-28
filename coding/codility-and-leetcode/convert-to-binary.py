# Convert to binary representation
def to_binary(A):
    bin = []
    if A == 0:
        return 0
    while A != 1:
        if A % 2 == 0:
            bin.append(str(0))
        else:
            bin.append(str(1))
        A = A / 2

    bin.append(str(1))
    return ''.join(bin[::-1])


print(to_binary(357))
print(to_binary(0))
print(to_binary(1))
print(to_binary(2))