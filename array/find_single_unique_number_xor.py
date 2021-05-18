def find_single(a):
    res = 0
    for index, num in enumerate(a):
        res ^= num
    
    return res

print(find_single([6,2,4,3,4,2,3]))