# initializing a 2d matrinx of W x n
wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
W = 9
n = 4

# add extra buffers
dp = [[-1]*5 for _ in range(10)]
def knapsack(wt, val, W, n):
    if n == 0 or W == 0:
        return 0

    if dp[W][n] != -1:
        return dp[W][n]

    if wt[n-1] <= W:
        dp[W][n] = max(val[n-1] + knapsack(wt, val, W-wt[n-1], n-1), 
                              knapsack(wt, val, W, n-1))
    else:
        dp[W][n] = knapsack(wt, val, W, n-1)

    return dp[W][n]


print(knapsack(wt, val, W, n))

##################################################################################
# iterative approach

from itertools import product

# add extra buffers
dp = [[0]*10 for _ in range(5)]
def knapsack(wt, val, W, n):
    """
    i : n
    j : w
    """
    for i, j in product(range(n+1), range(W+1)):
        if i==0 or j==0:
            dp[i][j] = 0

    for i, j in product(range(1, n+1), range(1, W+1)):
        if wt[i-1] <= j:
            dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]],
                           dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

    print(dp)
    return dp[n][W]
