# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None and t2 is None:
            return None
        elif t1 is None and t2 is not None:
            return t2
        elif t1 is not None and t2 is None:
            return t1
        else:
            tree = TreeNode(t1.val + t2.val)
            tree.left = self.mergeTrees(t1.left, t2.left)
            tree.right = self.mergeTrees(t1.right, t2.right)
            return tree