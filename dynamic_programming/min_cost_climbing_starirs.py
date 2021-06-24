from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        
        if n <= 1:
            return cost[n]

        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1] , dp[i-2])
            
        return min(dp[-1], dp[-2])



class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        return min(dp[len(cost) - 1], dp[len(cost) - 2])



s = Solution()
print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))