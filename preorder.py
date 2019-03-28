# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:

    def __init__(self):
        self.order = []

    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        self.order.append(root.val)
        for ch in root.children:
            self.preorder(ch)
        return self.order
