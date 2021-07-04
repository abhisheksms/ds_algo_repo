from itertools import product
def lps(a):
    """Return length of longest palindromic subsequence"""
    m = n = len(a)
    dp = [[0]*n for _ in range(m)]
    # initialize 
    for i, j in product(range(m), range(n)):
        if i == j:
            dp[i][j] = 1
        
    # fill
    for gap in range(1, n):
        for i in range(n - gap):
            j = i+gap
            
            if a[i] == a[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    for d in dp:
        print(d, end="\n")
    print()
 
    # return first row last column value
    return dp[0][-1]

print(lps("adceca")) #5