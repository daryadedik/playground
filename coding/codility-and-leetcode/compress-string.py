# Compress string
def compress1(S):
    if len(S) == 0:
        return ''
    compressed = []
    count = 1
    compressed.append(S[0])
    for i in range(len(S) - 1):
        if S[i + 1] == S[i]:
            count += 1
        else:
            compressed.append(count)
            count = 1
            compressed.append(S[i + 1])
    compressed.append(count)

    return ''.join(str(x) for x in compressed)

def compress2(S):
    S += '\0'

    compressed = []
    count = 1
    for i in range(len(S) - 1):
        if S[i + 1] == S[i]:
            count += 1
        else:
            compressed.append(S[i])
            compressed.append(count)
            count = 1

    return ''.join(str(x) for x in compressed)


def compress(S):
    S1 = compress1(S)
    S2 = compress2(S)
    assert(S1 == S2)
    return S1


print(compress(''))
print(compress('A'))
print(compress('AA'))
print(compress('ALDBRS'))
print(compress('AAADDDBBFALLLLSSHHH'))
print(compress('AK3'))
print(compress('1'))