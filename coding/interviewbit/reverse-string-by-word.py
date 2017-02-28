# Reverse the String

def reverseWords(S):
    S = S.split()

    for i in range(len(S) // 2):
        cur_i = S[i]
        S[i] = S[(i * -1) - 1]
        S[(i * -1) - 1] = cur_i
    return ' '.join(S)

print(reverseWords("the sky is blue"))
print(reverseWords(""))
print(reverseWords("the nat is always, nerveus"))
print(reverseWords("j"))