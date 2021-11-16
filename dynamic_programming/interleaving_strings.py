from itertools import product
def interleaved(X, Y, S):
    """
    The last character in S[i+j-1] should either be
          - X[i-1] or
          - Y[j-1]
    X - index j - represented as column
    Y - index i - represented as row

    
    -Not thinking about indexes
    -Going in autopilot mode while coding
    -1+1 = 2 - 1 gives last index
     So it should be i+j-1, not i+j-2
    """
    m, n = len(X)+1, len(Y)+1
    dp = [[False]*n for _ in range(m)]
    
    for i, j in product(range(m), range(n)):
        if i == 0 and j == 0:
            dp[i][j] = True
        elif i==0: 
            if X[j-1] == S[j-1]:
                dp[i][j] = True
        elif j==0: 
            if Y[i-1] == S[i-1]:
                dp[i][j] = True
        elif Y[i-1] == S[i+j-1]:
            dp[i][j] = dp[i-1][j]
        elif X[j-1] == S[i+j-1]:
            dp[i][j] = dp[i][j-1]
        else:
            pass
    
    print(dp)
    return dp[-1][-1]

X = "ABC"
Y = "DEF"
S = "ADEBFC"

if interleaved(X, Y, S):
    print("Given String is interleaving of X and Y")
else:
    print("Given String is a not interleaving of X and Y")