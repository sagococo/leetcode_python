from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        for x in A:
            if x%2 == 1:
                odd.append(x)
            else:
                even.append(x)

        result = []
        n = len(odd)
        for x in range(0, n):
            result.append(even[x])
            result.append(odd[x])
        return result