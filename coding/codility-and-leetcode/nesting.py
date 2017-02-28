# Codility. Nesting
def nesting(S):
    count = 0

    if not len(S):
        return 1

    for i in S:
        if i == '(':
            count += 1
        else:
            count -= 1
            if count < 0:
                return 0

    return 0 if count else 1

print(nesting('()()()'))
print(nesting('(()(())())'))
print(nesting('(()'))
print(nesting('((('))
print(nesting(''))
print(nesting('))(('))
print(nesting('(((('))
print(nesting(')()('))
print(nesting('(()()()()()())'))
print(nesting('('))
print(nesting('()((()())'))
print(nesting('())(()'))