from itertools import product
def isMatching(s, pattern):
    """
    dp[0][0] is true
    first row is false
    first col is false
    if ? or string and pattern match, check diagonally up
    if * look do or operation of left and up
    else it is false
    """
    row = len(s)+1
    col = len(pattern)+1
    
    dp = [[None]*(col) for _ in range(row)]
    
    # s[i] or pattern[j]
    for i, j in product(range(row), range(col)):
        if i==0 and j==0:
            dp[i][j] = True
        elif i==0 or j==0:
            dp[i][j] = False
        elif pattern[j-1] == "?" or s[i-1]==pattern[j-1]:
            dp[i][j] = dp[i-1][j-1]
        elif pattern[j-1] == "*":
            dp[i][j] = dp[i-1][j] or dp[i][j-1]
        else:
            dp[i][j] = False
        
    
    return dp[-1][-1]


s = "abcktde"
pattern = "a?c*t*"

if isMatching(s, pattern):
    print("Match")
else:
    print("No Match")