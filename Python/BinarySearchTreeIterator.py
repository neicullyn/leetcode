#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#O(n) Memory
# class BSTIterator:
#     # @param root, a binary search tree's root node
#     def LDR(self, root, lst):
#         if root is not None:
#             self.LDR(root.left, lst)
#             lst.append(root.val)
#             self.LDR(root.right, lst)
#             
#     def __init__(self, root):
#         self.lst = []
#         self.LDR(root, self.lst)
#         self.p = 0
#         self.n = len(self.lst)     
# 
#     # @return a boolean, whether we have a next smallest number
#     def hasNext(self):
#         return self.p < self.n
# 
#     # @return an integer, the next smallest number
#     def next(self):
#         r = self.lst[self.p]
#         self.p = self.p + 1
#         return r
    
#O(h) Memory
class BSTIterator:
    # @param root, a binary search tree's root node

    def __init__(self, root):
        self.stack = []
        self.p = root
        if self.p is not None:
            while self.p.left is not None:
                self.stack.append(self.p)
                self.p = self.p.left
            self.stack.append(self.p)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.p is not None

    # @return an integer, the next smallest number
    def next(self):
        r = self.p.val
        self.stack.pop()
        if self.p.right is not None:
            self.p = self.p.right
            while self.p.left is not None:
                self.stack.append(self.p)
                self.p = self.p.left
            self.stack.append(self.p)
        if len(self.stack) > 0:
            self.p = self.stack[-1]
        else:
            self.p = None
        return r

    
# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
root = TreeNode(10)
root.left = TreeNode(1)
root.left.right = TreeNode(8)
root.right = TreeNode(11)

i, v=BSTIterator(root),[]
while i.hasNext(): 
    v.append(i.next())
    print v
print v