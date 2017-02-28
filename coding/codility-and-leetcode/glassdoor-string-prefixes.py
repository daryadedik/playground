# find if strings are prefixes in a given string
def solution(S, D):
    if not S:
        return True
    return any(S.startswith(w) and solution(S[len(w):], D) for w in D)


def solution2(S, D):
    if not S:
        return True
    for w in D:
        if S.startswith(w) and solution(S[len(w):], D):
            return True
    return False

def solution1(S, D):
    if not S:
        return True
    for w in D:
        if S.startswith(w):
            found = solution(S[len(w):], D)
            if found:
                return True
    return False

print(solution('cdab', ['cd', 'l'])) #false
print(solution('cdabgrtd', ['cd', 'drtd'])) #false
print(solution('cdab', [])) #false
print(solution('cdab', ['a', 'b', 'c', 'd'])) #true
print(solution('', ['cd', 'l'])) #true
print(solution(' ', ['cd', 'l'])) #false