from itertools import product

# top down dp
def lcs_init(s1, s2, m, n):
    dp = [[0]*m for _ in range(n)]

    for i, j in product(range(m), range(n)):
        if not (i and j):
            dp[i][j] = 0

    return lcs(dp, s1, s2, m, n)

def lcs(dp, s1, s2, m, n):
    for i, j in product(range(1, m), range(1, n)):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    return dp[m-1][n-1]

s1 = "abcdef"
s2 = "aednek"
print(lcs_init(s1,s2,len(s1), len(s2)))