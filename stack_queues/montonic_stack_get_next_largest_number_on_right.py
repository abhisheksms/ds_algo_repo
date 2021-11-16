def monotonic_stack(height):
    """   
    Finding NEXT larger elements on the right, hence large elements are given preferrence
    """
    stack = []
    res = [0,0,0,0,0]
    
    index = 0
    n = len(height)
    # push first index first
    stack.append(0)
        
    for index in range(1, n):
        # if condtion satisfied
        while stack and height[index] > height[stack[-1]]:
            res[stack.pop()] = height[index]
            
        # we always have to append regardless of condition satisfied or not
        stack.append(index)

    return res

height=[9,6,10,7,9]
print(monotonic_stack(height))