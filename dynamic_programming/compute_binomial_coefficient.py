#recursive
def binomial(n, k):
    if k == 0 or k == n:
        return 1
    
    return binomial(n-1, k-1) + binomial(n-1, k)

# print(binomial(4, 2))

#iterative
def compute_binomial_coefficient(n,k):
    dp = [[0]*(k+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(min(i+1,k+1)):

            if j==0 or j==i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    print(dp)
    return dp[-1][-1]    


def binomial(n, k):
    dp = [[0]*(k+1) for _ in range(n+1)]

    for i in range(n+1):
        # for j in range(k+1):
        for j in range(min(i+1, k+1)): # same as above
            
            if j in (0, i):
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] 

    print(dp)
    return dp[-1][-1]

print(binomial(5,2))
# print(compute_binomial_coefficient(4, 2))
