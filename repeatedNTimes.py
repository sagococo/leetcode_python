from typing import List


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        lenth = len(A)/2
        unique = set(A)
        d = dict()
        for x in unique:
            d[x] = 0

        for x in A:
            d[x] = d[x] + 1

        for x in d.keys():
            if d[x] == lenth:
                return x

if __name__ == '__main__':
    list = [1,2,3,3]
    s = Solution()
    print(s.repeatedNTimes(list))