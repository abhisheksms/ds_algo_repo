class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """   
        Keep track of sums of all unique elements and store in a array
        Now apply house robber recurrence over the array
        """
        n = max(nums) + 1
        house = [0]*n
        dp = [0]*n
        for index, elem in enumerate(nums):
            house[elem] += elem
            
        dp[0], dp[1] = house[0], max(house[0], house[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], house[i]+dp[i-2])
        
        return dp[-1]