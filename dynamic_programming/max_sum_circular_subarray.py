class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """ 
        Case 2: If part of head and tail forms the max subarray
                Than the remaining subarray is the min subarray
                which can be computed by kadane algorithm
                
        However there is an edge case
        If all numbers are negative, maxSum = max(A) and minSum = sum(A).
        In this case, max(maxSum, total - minSum) = 0
        """
        # regular kadane
        maxc, maxg = nums[0], nums[0] 
        minc, ming = nums[0], nums[0]
        total = nums[0]
        for i in range(1, len(nums)):
            maxc = max(nums[i], nums[i]+maxc)
            maxg = max(maxc, maxg)
            minc = min(nums[i], nums[i]+minc)
            ming = min(minc, ming)
            total += nums[i]
        
        if maxg > 0:   
            return max(maxg, total - ming) 
        else: 
            return maxg #ie the highest negative number
        
        