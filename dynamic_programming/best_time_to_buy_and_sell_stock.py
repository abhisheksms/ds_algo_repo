#our_iterative
def best_time(a):
    dp = [0]*len(a)
    min_val = a[0]
    for i in range(1, len(a)):
        
        if a[i] < min_val:
            min_val = a[i]
        dp[i] = max(dp[i-1], a[i]-min_val)
    
    return dp[-1]


print(best_time([7,1,5,3,6,4]))
print(best_time([5,4,3,2,1,1]))
print(best_time([2,4,1]))