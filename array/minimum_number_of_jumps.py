def min_jumps(a):
    if len(a) <= 1 or a[0] == 0:
        return 0
        
    jumps = 1
    left, right = 0, a[0]

    while right < len(a) - 1:
        next_max = max(i+a[i] for i in range(left, right+1))
        jumps += 1
        left, right = right+1, next_max

    return jumps



print(min_jumps([1,1,1,1]))
print(min_jumps([2,3,1,1,4]))
print(min_jumps([1,3,5,8,9,2,6,7,6,8,9]))