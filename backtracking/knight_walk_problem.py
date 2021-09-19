class Node:
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist
         
def knight_walk(src, dest, N):
    """
    Time complexity: O(N^2). 
    Auxiliary Space: O(N^2).
    """
    queue = []
    # all possible movments for the knight
    row = [2, 2, -2, -2, 1, 1, -1, -1]
    col = [1, -1, 1, -1, 2, -2, 2, -2]
    
    visited = [[0]*N for _ in range(N)]
    
    # start = Node(src)
    visited[src.x][src.y] = 1
    queue.append(src)
    
    while queue:
        # remove first element
        val = queue.pop(0)
        if val.x == dest.x and val.y == dest.y:
            return val.dist

        for r, c in zip(row, col):
            new_x = val.x + r
            new_y = val.y + c
            
            if 0 <= new_x <= N-1 and 0 <= new_y <= N-1 and not visited[new_x][new_y]:
                visited[new_x][new_y] = 1
                queue.append(Node(new_x, new_y, val.dist+1))
                    
    return -1
    

N = 6
src = Node(2,3,0)
dest = Node(5,5,0)
print(knight_walk(src, dest, N))

src = Node(1,1,0)
dest = Node(30,30,0)
print(knight_walk(src, dest, 32))