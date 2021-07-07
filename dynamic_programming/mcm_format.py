def mcm(a, i, j):
    if i > j:
        return 0

    #for k in range(i+1, j) #i to k-1, k to j
    #for k in range(i, j-1)
    for k in range(i, j-1):
        
        temp_ans = mcm(a,i,k) + mcm(a, k+1, j) + (a[i-1]*a[j]*a[k])

        # ans = max(ans, temp_ans)
        ans = min(ans, temp_ans)

    return ans