def max_hist(a):
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


def max_rectangle(matrix):
    res = 0
    m, n = len(matrix), len(matrix[0])
    for i in range(1, m):
        for j in range(n):
            if matrix[i][j]:
                matrix[i][j] += matrix[i-1][j]
            
        res = max(res, max_hist(matrix[i][:]))
    
    return res

# print(max_hist([2,3,3,2]))
print(max_rectangle([[0,1,1,0],[1,1,1,1],[1,1,1,1],[1,1,0,0]]))