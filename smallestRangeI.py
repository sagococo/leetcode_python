from typing import List


class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        n_max = max(A)
        n_min = min(A)
        diff = n_max - n_min - 2 * K
        return max(0, diff)