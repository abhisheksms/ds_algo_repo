from itertools import product

# top down dp
def lcs_init(s1, s2, m, n):
    dp = [[0]*(m+1) for _ in range(n+1)]

    for i, j in product(range(m), range(n)):
        if not (i and j):
            dp[i][j] = 0

    return lcs(dp, s1, s2, m, n)

def lcs(dp, s1, s2, m, n):
    res = 0
    for i, j in product(range(1, m+1), range(1, n+1)):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = 0

        res = max(res, dp[i][j])

    print(dp)
    return res

# s1 = "abcdef"
# s2 = "aednek"

s1 = "abab"
s2 = "baba"
print(lcs_init(s1,s2,len(s1), len(s2)))