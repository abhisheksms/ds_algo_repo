def bin_search(a, val, low, high):
    mid = (low + high) // 2
    if a[mid] == val:
        return mid
    elif a[mid] > val:
        # left half
        return bin_search(a, val, low, mid-1)
    else:
        # right half
        return bin_search(a, val, mid+1, high)
    
    return -1

print(bin_search([1,2,3,4,5,6,7], 2, 0, 6)) #1
print(bin_search([1,2,3,4,5,6,7,10], 5, 0, 7)) # 4