class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        n = len(A)

        for x in range(0, n - 1):
            if A[x] > A[x + 1]:
                return x
        return n - 1
