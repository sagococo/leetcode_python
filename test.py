from typing import List


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        lenth = len(A)/2
        unique = set(A)

        for x in unique:
            count = 0
            for y in A:
                if x == y:
                    count += 1
            if count == lenth:
                return x

if __name__ == '__main__':
    di = dict()
    print(di[1])