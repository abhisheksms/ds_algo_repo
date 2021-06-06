from itertools import product
# a = [3,34,4,12,5,2]
# sum = 9

# a = [2,3,7,8,11]
# sum = 10

a = [2,3,5,6,8,10]
sum = 10
n = len(a)
row = n+1
col = sum+1

dp = [[0]*col for _ in range(row)]
def count_subset_sum(a, sum):
    for i in range(row):
        dp[i][0] = 1

    # 1 since 1st column is already initializes and 1st row will always be zero
    for i,j in product(range(1, row), range(1, col)):
        # dp[i-1][j-a[i-1]] : Included
        # dp[i-1][j] : Excluded
        if a[i-1] <= j:
            dp[i][j] = dp[i-1][j-a[i-1]] + dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]

    print(dp)
    return dp[n][sum]

    


print(count_subset_sum(a, sum))