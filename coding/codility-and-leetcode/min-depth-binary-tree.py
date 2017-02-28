# 111.Minimum Depth of Binary Tree. Leetcode
def minDepth(root, l=0):
    if not root:
        return l
    if not root.left:
        return minDepth(root.right, l+1)
    elif not root.right:
        return minDepth(root.left, l+1)
    return min(minDepth(root.left, l+1), minDepth(root.right, l+1))

from collections import deque
def minDepth2(self, root):
        if not root:
            return 0
        q = deque([(root, 1)])
        while q:
            first, l = q.popleft()
            if first:
                if not first.right and not first.left:
                    return l
                q.append((first.left, l+1))
                q.append((first.right, l+1))

def dfs(self, root):
        stack = [root]
        while stack:
            last = stack.pop()
            if last:
                print last.val
                stack.append(last.left)
                stack.append(last.right)

def dfs_levels(self, root):
        stack = [(root, 1)]
        while stack:
            last, l = stack.pop()
            if last:
                print last.val, l
                stack.append((last.left, l+1))
                stack.append((last.right, l+1))

def bfs(self, root):
        q = deque([(root, 1)])
        while q:
            last, l = q.popleft()
            if last:
                print last.val, l
                q.append((last.left, l+1))
                q.append((last.right, l+1))