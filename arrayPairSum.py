class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        sum = 0
        for x in range(0, n, 2):
            sum += nums[x]
        return sum