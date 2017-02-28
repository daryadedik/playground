# fund if string is a palindrome
def isPalindrome(S):
    for i in S[::-1]:
        print(i)
    return S == S[::-1]

def isPalindrome2(S):
    pali = True
    for i in range (0, len(S) // 2):
        if S[i] == S[(i * -1) - 1] and pali is True:
            pali = True
        else:
            pali = False
    return pali

print(isPalindrome('hjhghjhg'))