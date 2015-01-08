# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root is None:
            return 0
        if root.left is not None:
            l = self.maxDepth(root.left)
        else:
            l = 0
        if root.right is not None:
            r = self.maxDepth(root.right)
        else:
            r = 0
        return max(l,r)+1