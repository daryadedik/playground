# Implement stack
size = 0

def init_stack(N):
    return [0] * N

def push(x, stack):
    global size
    stack[size] = x
    size += 1

def pop(stack):
    global size
    size -= 1
    stack[size] = 0
    return stack[size]

cur_stack = init_stack(10)
push(5, cur_stack)
push(7, cur_stack)
pop(cur_stack)
print(cur_stack)