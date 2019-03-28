# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:

    def __init__(self):
        self.order = []

    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        for ch in root.children:
            self.postorder(ch)

        self.order.append(root.val)
        return self.order