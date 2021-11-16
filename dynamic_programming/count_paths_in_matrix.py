from itertools import product
def numberOfPaths(m, n):
    dp = [[0]*(n) for _ in range(m)]
    for i,j in product(range(m), range(n)):
        if i == 0 or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j] +dp[i][j-1]
            
    return dp[-1][-1]

m = 4
n = 4
print(numberOfPaths(m, n)) 