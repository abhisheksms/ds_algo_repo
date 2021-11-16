class Solution:
    def rob(self, nums: List[int]) -> int:
        """ 
        # I can skip by more than one, not necessarily by one
        # what are all the candidates
        # dp[n-1] and nums[n] + dp[n-2] 

        - A robber has 2 options: 
          a) rob current house i; 
          b) don't rob current house.

        - If an option "a" is selected it means she can't rob previous i-1 house 
        but can safely proceed to the one before previous i-2 and gets all cumulative loot that follows.

        - If an option "b" is selected the robber gets all the possible loot from 
        robbery of i-1 and all the following buildings. 

        [1,400, 1, 1, 100, 2, 100, 1] # 600
        [100, 2, 4, 100] # 200
        """
        
        n = len(nums)
        if n <= 1:
            return max(nums)
        
        dp = [0]*n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
        
        
        return dp[-1]