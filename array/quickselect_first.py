def quickselect(a, k):
    n = len(a)
    for p in range(n):
        count = 0
        for i in range(n):
            if a[i] < a[p]:
                count+=1

        if count + 1 == k:
            return a[p]


print(quickselect([5,3,2,1,4], 2))