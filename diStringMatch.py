from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        upper = 1
        lower = -1
        result = [0, ]
        for x in S:
            if x == 'I':
                result.append(upper)
                upper += 1
            else:
                result.append(lower)
                lower -= 1

        seq = []

        for x in result:
            t = x + (-1) * lower - 1
            seq.append(t)
            return seq