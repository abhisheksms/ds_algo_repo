"""
if n is even
number of bits same as n//2

if n is odd
number of bits is n//2 + 1
Since LSB is set and we are performing a right shift 
      when we divide by 2
"""
# recursion with memoization
from typing import List
class Solution:
    def __init__(self):
        self.hash_map = {}

    def perform_recursion(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n in self.hash_map:
            return self.hash_map[n]
        elif n%2 == 0:
            self.hash_map[n] = self.perform_recursion(n//2)
        else:
            self.hash_map[n] = self.perform_recursion(n//2) + 1

        return self.hash_map[n]

    def countBits(self, n: int) -> List[int]:
        res = [self.perform_recursion(i) for i in range(n+1)]
        return res


# iterative
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            if i%2 == 0:
                dp[i] = dp[i//2]
            else:
                dp[i] = dp[i//2] + 1

        return dp
 
s = Solution()
print(s.countBits(5))