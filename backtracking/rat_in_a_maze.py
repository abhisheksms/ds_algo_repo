global N
def rat_maze(maze, i, j, res):
    if i == N - 1 and j == N -1:
        print(res)
        return
    
    if i < N and j+1 < N and maze[i][j+1] == 0:
        res.append([i, j+1])
        rat_maze(maze, i, j+1, res)
        res.pop()

    if i+1 < N and j < N and  maze[i+1][j] == 0:
        res.append([i+1, j])
        rat_maze(maze, i+1, j, res)
        res.pop()


maze = [ [0, 1, 0, 1, 1], 
         [0, 0, 0, 0, 0], 
         [1, 0, 1, 0, 1], 
         [0, 0, 1, 0, 1], 
         [1, 0, 1, 0, 0]
         ]
N = 5
print(rat_maze(maze, 0, 0, [[0,0]]))