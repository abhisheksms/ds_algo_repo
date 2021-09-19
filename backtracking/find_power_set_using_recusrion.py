global N
def power_set(res, a, index):
    print(res)
    for i in range(index, N):
        res.append(a[i])
        power_set(res, a, i+1)
        res.pop()
        

a = [1,2,3]
N = len(a)
power_set([], a, 0)