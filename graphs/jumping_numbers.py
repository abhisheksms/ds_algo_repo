from collections import deque
def jumping_numbers(x):
    """
    - next jumping numbers to 23 is 
        232 = 23*10 + 2
        234 = 23*10 + 4
   - zero based exception: when the last number is zero
                           we can only use lastdigit + 1
   - nine based exception: when the last number is nine
                           we can only use lastdigit - 1
    """
    res = []
    d = deque()
    
    for i in range(1, 10):
        if i < x:
            d.append(i)
        
    while d:
        val = d.popleft()
        res.append(val)
        
        last_num = val % 10
        if last_num != 0:
            new_val = val*10 + (last_num-1)
            if new_val < x:
                d.append(new_val)
        
        if last_num != 9:
            new_val = val*10 + (last_num+1)
            if new_val < x:
                d.append(new_val)
    
    return res
    

x = 65
print(jumping_numbers(x))