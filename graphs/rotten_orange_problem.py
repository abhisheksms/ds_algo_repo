from itertools import product
from collections import namedtuple, deque

orange = namedtuple("orange", ["x", "y", "time"])  

def is_fresh_present(matrix):
    for i,j in product(range(3), range(5)):
        if matrix[i][j] == 1:
            return True
    
    return False


def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 5


def rotten_orange(matrix):
    row = [1,-1,0,0]
    col = [0,0,-1,1]
    
    res_time = 0
    d = deque()
    
    # first add all rotten oranges to matrix
    for i,j in product(range(3), range(5)):
        if matrix[i][j] == 2:
            d.append(orange(i,j,0))
            
    while d:
        val = d.popleft()
        res_time = val.time
        
        for x, y in zip(row, col):
            new_x = val.x + x
            new_y = val.y + y
            
            if is_valid(new_x, new_y) and matrix[new_x][new_y] == 1:
                d.append(orange(new_x, new_y, val.time + 1))
                # No need for visited as we are marking position as rotten
                matrix[new_x][new_y] = 2
        
    if is_fresh_present(matrix):
        return -1
    else:      
        return res_time
                
            
print(rotten_orange([[2,1,0,2,1],
                    [1,0,1,2,1],
                    [1,0,0,2,1]])) 