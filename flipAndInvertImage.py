from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for x in A:
            x.reverse()
        for x in A:
            for y in x:
                if y == 1:
                    y = 0
                if y == 0:
                    y = 1
        print(A)