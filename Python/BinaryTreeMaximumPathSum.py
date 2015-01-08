class Solution:
    # @param root, a tree node
    # @return an integer
    def getMaxDepth(self, root):
        if root is None:
            return 0
        else:
            return root.max_depth
    
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            root.max_depth = max(self.maxDepth(root.left), self.maxDepth(root.right), 0) + root.val
            return root.max_depth
        
    def maxPathSum(self, root):
        self.maxDepth(root)
        return self._maxPathSum(root)   
     
    def _maxPathSum(self, root):
        if root is None:
            return -2147483648
        a = max(self.getMaxDepth(root.left), 0) + max(self.getMaxDepth(root.right), 0) + root.val
        b = self._maxPathSum(root.left)
        c = self._maxPathSum(root.right)
        return max(a, b, c)
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
r = TreeNode(1)
r.left = TreeNode(2)
print Solution().maxPathSum(r)

r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(-2)
print Solution().maxPathSum(r)

r = TreeNode(-3)
print Solution().maxPathSum(r)