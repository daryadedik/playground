# Longest substring
def longest_substr(A, B):
    max_substr = []

    if len(A) == 0 or len(B) == 0:
        return -1

    max_len = 0
    for i in range(len(A)):
        for j in range(len(B)):
            length = 0
            substr = []
            k = 0
            while i + k < len(A) and j + k < len(B) and A[i + k] == B[j + k]:
                substr.append(A[i + k])
                length += 1
                k += 1
            if length > max_len:
                max_len = length
                max_substr = ''.join(substr)
            j = j + k
    return (max_len, max_substr)

A_str = "dsddashadl"
B_str = "liydashads"

lsubstr = longest_substr(A_str, B_str)
print("Longest substring length: {}".format(lsubstr[0]))
print("Longest substring: {}".format(lsubstr[1]))