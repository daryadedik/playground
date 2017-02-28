# Palindrome String

def isPalindrome(A):
    A = ''.join([i.lower() for i in A if i.isalnum()])
    print(A)
    pali = 1
    for i in range(len(A) // 2):
        if A[i] != A[(i * -1) - 1]:
            return 0
    return pali

print(isPalindrome('Race, a car'))
print(isPalindrome(''))
print(isPalindrome('1a2'))