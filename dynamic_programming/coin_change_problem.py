from itertools import product
def coin_change(dp, a, sum, n):
    row = n
    col = sum
    for i,j in product(range(1, row), range(1, col)):
        if a[i-1] <= j:
            dp[i][j] = dp[i-1][j] + dp[i][j-a[i-1]]
        else:
            dp[i][j] = dp[i-1][j]

    # print(dp)
    return dp[row-1][col-1]

def init_coin_change(a, sum, n):
    dp = [[0]*sum for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1

    return coin_change(dp, a, sum, n)

# a = [2,3,4]
# sum = 7

a = [1,2,5]
sum = 11

print(init_coin_change(a, sum, len(a)))