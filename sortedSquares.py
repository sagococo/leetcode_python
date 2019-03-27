from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        squares = []
        for x in A:
            squares.append(x * x)
        return sorted(squares)