# 404. Sum of Left Leaves. Leetcode
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root, is_left=False):
        if root == None or root.left == None and root.right == None and not is_left:
            return 0
        if root.left == None and root.right == None and is_left:
            return root.val
            
        return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right, False)

Solution(TreeNode([1,2,10,None,None,15,12,1,12]))