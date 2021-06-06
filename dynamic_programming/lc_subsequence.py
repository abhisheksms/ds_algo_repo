# iterative
from itertools import product
dp = [[-1]*8 for _ in range(7)]
def lcs_iterative(x,y,m,n):
    for i, j in product(range(m+1), range(n+1)):
        # if i==0 or j==0:
        #     dp[i][j]=0
        if not (i and j):
            dp[i][j] = 0

    for i, j in product(range(1, m+1), range(1, n+1)):
        if x[i-1] == y[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # print(dp)
    return dp[m][n]
    

# memoized
dp = [[-1]*8 for _ in range(7)]
def lcs_memo(x,y,m,n):
    # if n==0 or m==0:
    #     return 0

    # demorgan's law
    if not all([n,m]):
        return 0

    if dp[m][n] != -1:
        return dp[m][n]

    
    if x[m-1] == y[n-1]:
        dp[m][n] = 1 + lcs_memo(x,y,m-1,n-1)
    else:
        dp[m][n] = max(lcs_memo(x,y,m,n-1), lcs_memo(x,y,m-1,n))
    
    # only for printing o/p matrix
    a = m==5
    b = n==6
    if all([a,b]):
        for i in range(m+1):
            for j in range(n+1):
                print(dp[i][j], end=" ")
            print()
    return dp[m][n]

    

# # recursive
def lcs_recursive(x,y,m,n):
    # if n==0 or m==0:
    #     return 0

    # if not all([n,m]):
    #     return 0

    if not (n and m):
        return 0

    if x[m-1] == y[n-1]:
        return 1 + lcs_recursive(x,y,m-1,n-1)
    else:
        return max(lcs_recursive(x,y,m,n-1), lcs_recursive(x,y,m-1,n))

# -1 from actual length
print(lcs_iterative("abcdgh", "abcdfhr",6, 7))
print(lcs_memo("abcdgh", "abcdfhr",6, 7))
print(lcs_recursive("abcdgh", "abcdfhr",6, 7))
# print(lcs("abcdaf", "acbcf", 5, 4))
