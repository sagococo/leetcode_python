from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        for x in A:
            if x%2 == 0:
                even.append(x)
            if x%2 == 1:
                odd.append(x)
        return even + odd