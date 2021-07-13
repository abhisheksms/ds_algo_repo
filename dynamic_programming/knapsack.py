def knapsack_with_repetion(wt, val, W, n):
    """
    Unbounded knapsack
    """
    # knapsack array of length W+1
    kw = [0]*(W+1)

    # kw[0] : knapsack with weight 0
    for w in range(1, W+1):
        for i in range(n):
            if wt[i] <= w:

                # k(w) = max(k(w - w[i]) + v[i])
                kw[w] = max(kw[w], kw[w-wt[i]] + val[i])

    print(kw)
    return kw[-1]

#######################
# W = 100
# val = [10, 30, 20]
# wt = [5, 10, 15]
# n = len(val)
# print(knapsack_with_repetion(wt, val, W, n))


from itertools import product
def knapsack_without_repetion(wt, val, W, n):
    dp = [[0]*(n+1) for _ in range(W+1)]

    i : W(wt)
    j : n(val)
    for i,j in product(range(W+1), range(n+1)):
        # if not (i and j)
        if i==0 or j==0:
            dp[i][j] = 0
        elif wt[j-1]<=i:
            dp[i][j] = max(dp[i][j-1], val[j-1]+dp[i-wt[j-1]][j-1])
        else:
            dp[i][j] = dp[i][j-1]

    print(dp)  
    return dp[W][n]


wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
W = 9
n = 4
print(knapsack_without_repetion(wt, val, W, n))