class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Divide into 2 sub problems
        1. Index 0 to n-1
        2. Index 1 to n

        Then solve using house robber 1
        """
        n = len(nums)
        if n <= 2:
            return max(nums)
        else:
            dp = [0]*n
            # case 1 index 0 to n-1
            dp[0], dp[1] = nums[0], max(nums[0], nums[1])
            for i in range(2, n-1):
                dp[i] = max(dp[i-1], nums[i]+dp[i-2])
            
            first = dp[-2]
            
            # case 2 index 1 to n
            dp[1], dp[2] = nums[1], max(nums[1], nums[2])
            for i in range(3, n):
                dp[i] = max(dp[i-1], nums[i]+dp[i-2])
                
            second = dp[-1] 
            return max(first, second)