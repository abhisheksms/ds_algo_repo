from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = max_global = nums[0]
        print(f"nums[0] {nums[0]}, max_current {max_current}, max_global {max_global}")
        for i in range(1, len(nums)):
            max_current = max(nums[i], nums[i]+max_current)
            max_global = max(max_current, max_global)

            print(f"nums[{i}] {nums[i]}, max_current {max_current}, max_global {max_global}")
        return max_global

s = Solution()
print(s.maxSubArray([-2,3,2,-1]))
print(s.maxSubArray([1,-3,2,1,-1]))