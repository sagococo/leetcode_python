from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        string = A[0]
        result = []
        for x in string:
            for s in A:
                if x not in s:
                    continue
                else:
                    A.s = s.replace(x, '', 1)
            result.append(x)
        return result