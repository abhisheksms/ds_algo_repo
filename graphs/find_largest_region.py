from itertools import product
from collections import deque
global visited, island, d, N
N = 5

visited = [[0]*N for _ in range(N)]
island = [[0,0,1,1,1],
          [1,0,1,1,0],
          [0,1,0,0,0],
          [0,0,0,0,1],
          [0,0,1,1,0]]

row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]
d = deque()


def bfs():
    val = 0
    while d:
        x, y = d.popleft()
        visited[x][y] = 1
        val += 1
        for ib, jb in zip(row,col):
            new_x = x+ib
            new_y = y+jb
            
            if  0 <= new_x < N and 0 <= new_y < N:

                # addditional condition here as compared to knight walk problem
                if island[new_x][new_y] and not visited[new_x][new_y]:
                    d.append([new_x, new_y])
                    visited[new_x][new_y] = 1
                    
    return val


def get_max_area():
    res = 0
    for ib, jb in product(range(N), range(N)):
        if island[ib][jb] and not visited[ib][jb]:
            d.append([ib,jb])
            res = max(res, bfs())
        
    return res


print(get_max_area())