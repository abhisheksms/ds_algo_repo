def left_zero(a, low, high):
    mid = (low + high) // 2
    #mid = low + (high - low) // 2 # to avoid overflow
    
    if a[mid-1] < a[mid] or mid == 0: # 0 1 1
        return mid
    elif a[mid] == 0: #0 0 0
        #right half
        return left_zero(a, mid+1, high)
    else:
        # left half
        return left_zero(a, low, mid-1)

    return len(a)


# print(left_zero([0,0,0,0,0,1,1], 0, 6)) # 5
# print(left_zero([0,0,1,1,1,1,1], 0, 6)) #2
# print(left_zero([1,1,1,1], 0, 3)) # 0

def max_row(d):
    min_one_index = 0
    min_val = len(d)

    low = 0
    high = len(d) - 1

    for index, row in enumerate(d):
        val = left_zero(row, low, high)
        if val < min_val:
            min_val = val 
            min_one_index = index

    return min_one_index


print(max_row([[0, 1, 1, 1], 
               [0, 0, 1, 1], 
               [0, 0, 0, 1], 
               [1, 1, 1, 1]])) # 3


