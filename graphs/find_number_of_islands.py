from itertools import product
from collections import deque
global visited, island, d, N
N = 5

visited = [[0]*N for _ in range(N)]
island = [[0,0,1,1,0],
          [1,0,1,1,0],
          [0,1,0,0,0],
          [0,0,0,0,1],
          [0,0,1,1,0]]

row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]
d = deque()


def bfs():
    while d:
        x, y = d.popleft()
        #print(x,y)
        visited[x][y] = 1

        for ival,jval in zip(row, col):
            new_x = x+ival
            new_y = y+jval
            #print("New values", new_x, new_y)
            if 0 <= new_x < N and 0 <= new_y < N:
                if island[new_x][new_y] and not visited[new_x][new_y]:
                    visited[x+ival][y+jval] = 1
                    d.append([new_x,new_y])


def check_connected_components():
    """
    Time Complexity: O(m*n) m rows n columns
    """
    res = 0
    for i, j in product(range(N), range(N)):
        if island[i][j] and not visited[i][j]:
            d.append([i,j])
            bfs()
            res += 1
    return res


print(check_connected_components())