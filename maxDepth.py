# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        else:

            if len(root.children) == 0:
                return 1

            depth = []
            for x in root.children:
                depth.append(self.maxDepth(x))
            return 1 + max(depth)
