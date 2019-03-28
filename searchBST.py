# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None

        if root.val == val:
            return root
        left = self.searchBST(root.left, val)
        right = self.searchBST(root.right, val)

        if left is not None:
            return left
        if right is not None:
            return right

        return None