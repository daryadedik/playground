# Codility. Brackets
def push(val, stack, size):
    stack[size] = val
    size += 1
    return size

def pop(stack, size):
    size -= 1
    stack[size] = 0
    return size

def brackets(S):
    if not len(S):
        return 1
    size = 0
    stack = [0] * len(S)
    size = push(S[0], stack, size)
    for i in range(1, len(S)):
        if S[i] == ')' and stack[size-1] == '(' \
        or S[i] == ']' and stack[size-1] == '[' \
        or S[i] == '}' and stack[size-1] == '{':
            size = pop(stack, size)
        else:
            size = push(S[i], stack, size)

    return 1 if not stack[0] else 0

print(brackets('[[()()]]'))
print(brackets('[[()]]'))
print(brackets('[(]{})]'))
print(brackets('{{]]}'))
print(brackets('[][][]'))
print(brackets('{{]]}'))