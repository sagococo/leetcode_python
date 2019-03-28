from typing import List


class Solution:

    def __init__(self):
        self.list = []

    def isOK(self, c):
        for x in range(0, len(self.list)):
            if c in self.list[x]:
                self.list[x] = self.list[x].replace(c, '', 1)
            else:
                return False
        return True

    def commonChars(self, A: List[str]) -> List[str]:
        n = len(A)
        string = A[0]
        result = []
        self.list = A
        for x in string:
            if self.isOK(x):
                result.append(x)
        return result
