global N 
N = 4

def is_safe(board, row, col):
    # left row
    for i in range(col):
        if board[row][i]:
            return False
    
    # principal diagonal (moves up)
    for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[r][c]:
            return False

    # secondary diagonal
    for r, c in zip(range(row, N), range(col, -1, -1)):
        if board[r][c]:
            return False
    
    return True

def nqueen(board, col):
    
    if col >= N:
        return True
    
    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            
            if nqueen(board, col+1) == True:
                return True
            
            board[row][col] = 0
            
    
    return False
            
       
board = [ [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0] ]
# start from 0th col
if nqueen(board, 0):
    print(board)
else:
    print("No solution")