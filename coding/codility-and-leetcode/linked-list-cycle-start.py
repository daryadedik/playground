# 142. Linked List Cycle II. Leetcode. Find start of cycle
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def cycle_start(head):
    if not head or not head.next:
        return None
    s = f = head
    while f and f.next:
        s = s.next
        f = f.next.next
        if s == f:
            break
    if s != f:
        return None
    count = 1
    while s.next != f:
        count += 1
        s = s.next
    f = s = head
    while count:
        f = f.next
        count -= 1
    while s != f:
        s = s.next
        f = f.next
    return s

linkedlist = ListNode(9)
linkedlist2 = ListNode(6)
linkedlist3 = ListNode(4)
linkedlist4 = ListNode(2)
linkedlist.next = linkedlist2
linkedlist2.next = linkedlist3
linkedlist3.next = linkedlist4
linkedlist4.next = linkedlist2

print cycle_start(linkedlist)