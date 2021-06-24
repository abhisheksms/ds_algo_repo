# DP: incorrect in leetcode
from itertools import product
class Solution:
    def sub_init(self, s1, s2, m, n):
        dp = [[0]*n for _ in range(m)]

        for i, j in product(range(m), range(n)):
            if j == 0:
                dp[i][j] = 0
            if i == 0:
                dp[i][j] = 1
            
        return self.sub(dp, s1, s2, m, n)

    def sub(self, dp, s1, s2, m, n):
        for i, j in product(range(1, m), range(1, n)):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1] and dp[i-1][j]

        return bool(dp[m-1][n-1])

    def isSubsequence(self, s1: str, s2: str) -> bool:
        return self.sub_init(s1,s2,len(s1)+1, len(s2)+1)

# 2- pointer
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x = y = 0
        m = len(s)
        n = len(t)

        while x < m and y < n:
            if s[x] == t[y]:
                x += 1

            y += 1


        if x == m:
            return True
        else:
            return False
        

s = Solution()
print(s.isSubsequence("ab", "acbf"))
print(s.isSubsequence("ace", "abcdef"))
print(s.isSubsequence("aec", "abcdef"))
print(s.isSubsequence("az", "abcdef"))
print(s.isSubsequence("axc", "ahbgdc"))
