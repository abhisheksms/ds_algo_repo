import time
# recursive
def climb_rec(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return climb_rec(n-1) + climb_rec(n-2)

# recursive with memoization
hash_map = {}
def climb_memo(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n in hash_map:
        return hash_map[n]
    else:
        hash_map[n] = climb_memo(n-1) + climb_memo(n-2)
        return hash_map[n]


def climb_iter(n):
    """
    index 0: 1 stair
    index 1: 2 stairs
    """
    dp = [0]*n
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i-2] + dp[i-1]

    return dp[-1]

rec_time = time.time()
print(climb_rec(35))
print("Time take for recursive approach ", time.time()-rec_time, " seconds")

memo_time = time.time()
print(climb_memo(35))
print("Time take for recursion with memoization approach ", time.time()-memo_time, " seconds")

iter_time = time.time()
print(climb_iter(35))
print("Time take for iterative approach ", time.time()-iter_time, " seconds")

## You can reach stair n only through stair n-1 and stair n-2
## The number of ways to reach stair n 
## is the sum of ways to reach stair n-1 + sum of ways to reach stair n-2

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        dp = [0]*n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-2] + dp[i-1]

        return dp[-1]
