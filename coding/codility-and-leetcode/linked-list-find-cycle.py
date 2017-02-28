# 142. Linked List Cycle II. Leetcode. Find if there is a cycle
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle2(self, head):
    arr = []
    while head and head not in arr:
        arr.append(head)
        print head.val
        head = head.next

from collections import defaultdict

def hasCycle3(head):
    d = defaultdict(int)
    while head:
        print head.val
        d[head] += 1
        if d[head] == 2:
            return 1
        head = head.next
    return 0

def hasCycle4(head):
    s = set()
    while head and head not in s:
        print head.val
        s.add(head)
        head = head.next
    return head is not None

def hasCycle(head):
    s = f = head
    while f and f.next:
        print s.val, f.val
        s = s.next
        f = f.next.next
        if s == f:
            return True
    return False

linkedlist = ListNode(9)
linkedlist2 = ListNode(6)
linkedlist3 = ListNode(4)
linkedlist4 = ListNode(2)
linkedlist.next = linkedlist2
linkedlist2.next = linkedlist3
linkedlist3.next = linkedlist4
linkedlist4.next = linkedlist2

print hasCycle(linkedlist)

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = {}
for k, v in s:
    if k not in d:
        d[k] = []
    d[k].append(v)
print(d.items())