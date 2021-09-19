def max_rectangular_area(a):
    n = len(a)
    stack = []
    
    # represents the index 
    # which describles HOW MANY ELEMENTS IN THE ARRAY
    # have been SEEN so far
    index = 0
    res = 0
    
    while index < n:
        if (not stack) or (a[index] >= a[stack[-1]]):
            stack.append(index)
            index+=1
        else:
            top_val = stack.pop()
            one = a[top_val]
            if stack:                 
                two = index - stack[-1] - 1
            else:
                # for empty stack
                two = index
            
            res = max(res, one*two)
            
    while stack:
        top_val = stack.pop()
        one = a[top_val]
        if stack:
            two = index - stack[-1] - 1
        else:
            # for empty stack
            two = index
            
        res = max(res, one*two)

        
    return res