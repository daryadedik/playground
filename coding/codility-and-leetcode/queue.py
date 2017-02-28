# Queue implementation
head, tail = 0, 0

def init_queue(N):
    return [0] * N

def push(x, queue):
    global tail
    tail = (tail + 1) % len(queue)
    queue[tail] = x

def pop(queue):
    global head
    head = (head + 1) % len(queue)
    queue[head] = 0
    return queue[head]

def size(queue):
    return (tail - head + len(queue)) % len(queue)

def empty():
    return head == tail

size = 0
cur_queue = init_queue(10)
push(1, cur_queue)
push(2, cur_queue)
push(3, cur_queue)
push(4, cur_queue)
push(5, cur_queue)
push(6, cur_queue)
push(7, cur_queue)
push(8, cur_queue)
push(9, cur_queue)
push(10, cur_queue)
push(11, cur_queue)
pop(cur_queue)
print(cur_queue)