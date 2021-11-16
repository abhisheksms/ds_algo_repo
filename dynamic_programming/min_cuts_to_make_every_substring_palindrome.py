from itertools import product
def min_cuts(a):
    """Return length of longest palindromic subsequence"""
    m = n = len(a)
    dp = [[0]*n for _ in range(m)]
        
    # fill
    for gap in range(1, n):
        for i in range(n - gap):
            j = i+gap
            
            val = min(dp[i+1][j], dp[i][j-1])
            
            if a[i] == a[j]:
                dp[i][j] = max(0, val - 1) # to avoid -ve values fron being assigned
            else:
                dp[i][j] = val + 1

    for d in dp:
        print(d, end="\n")
    print()
 
    # return first row last column value
    return dp[0][-1]

print(min_cuts("bcdck")) #5


class Solution:
    def minCut(self, a: str) -> int:
        m = n = len(a)
        dp = [[0]*n for _ in range(m)]
            
        # fill
        for gap in range(1, n):
            for i in range(n - gap):
                j = i+gap
                
                val = min(dp[i+1][j], dp[i][j-1])
                
                if a[i] == a[j]:
                    dp[i][j] = max(0, val - 1) # to avoid -ve values fron being assigned
                else:
                    dp[i][j] = val + 1

        # return first row last column value
        return dp[0][-1]