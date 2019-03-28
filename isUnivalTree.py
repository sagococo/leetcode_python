# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root.left is None and root.right is None:
            return True
        elif root.left is not None and root.right is None:
            return root.left.val == root.val and self.isUnivalTree(root.left)
        elif root.left is None and root.right is not None:
            return root.right.val == root.val and self.isUnivalTree(root.right)
        else:
            return root.right.val == root.val and root.left.val == root.val and self.isUnivalTree(root.left) and self.isUnivalTree(root.right)