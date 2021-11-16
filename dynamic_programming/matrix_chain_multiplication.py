def mcm(a, i, j):
    n = j+1
    dp = [[0]*n for _ in range(n)]

    for gap in range(1, n):
        for i in range(n - gap):
            j = i+gap
            
            ans = 1000000
            for k in range(i, j-1):
                temp_ans = dp[i][k] + dp[k+1][j] + (a[i-1]*a[k]*a[j])
                print(temp_ans)
                ans = min(ans, temp_ans)

            dp[i][j] = ans

    print(dp)
    return dp[0][-1]


# i or i+1
# where does array start and end
# dry run??

print(mcm([50,20,1,10,100], 0, 4))