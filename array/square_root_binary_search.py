def get_root(n, low, high):
    mid = (low + high) // 2
    if mid ** 2 <= n:
        return mid
    else:
        return get_root(n, low, mid)

        
def sqr_root(n):
    low = 1
    high = n
    return get_root(n, low, high)


print(sqr_root(10)) #3
print(sqr_root(64))
print(sqr_root(3)) #1
print(sqr_root(1))