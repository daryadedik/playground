# 203. Remove Linked List Elements. Leetcode

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        f = ListNode(0)
        f.next = head
        g = f
        while g and g.next:
            ng = g.next
            while ng and ng.val == val:
                ng = ng.next
            g.next = ng
            g = ng
        return f.next