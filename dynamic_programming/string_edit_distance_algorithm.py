from itertools import product

def edit_distance(dp, s1, s2, n1, n2):
    for i, j in product(range(1, n1), range(1, n2)):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

    #print(dp)
    return dp[n1-1][n2-1]

def init_edit_distance(s1, s2, n1, n2):
    dp = [[0]*n2 for _ in range(n1)]

    # column: source
    # row: destination

    # first row: insertion
    # first col: deleteion
    for i, j in product(range(n1), range(n2)):
        if i == 0:
            dp[i][j] = j
        
        if j == 0:
            dp[i][j] = i

    return edit_distance(dp, s1, s2, n1, n2)

s1 = "sunday"
s2 = "saturday"
print(init_edit_distance(s1, s2, len(s1), len(s2)))
