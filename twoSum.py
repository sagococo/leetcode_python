from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for x in range(n):
            num = nums[x]

            for y in range(x + 1, n):
                if num + nums[y] == target:
                    return [x, y]

