# 104. Maximum Depth of Binary Tree. Leetcode
from collections import deque

def maxDepth(self, root):
        q, l = deque([(root, 0)]), 0
        while q:
            f, l = q.popleft()
            if f:
                q.append((f.left, l+1))
                q.append((f.right, l+1))
        return l

def maxDepth_recursive(self, root, l=0):
    if not root:
        return l
    return max(self.maxDepth(root.left, l+1), self.maxDepth(root.right, l+1))