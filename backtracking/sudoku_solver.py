def print_grid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()

        
def find_empty_space(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j) # row, then column of empty spaces.
    return None


def check_occupied(num, row, col):
    sector = 3*(row//3) + (col//3)
    return not check_row[row][num] and not check_col[col][num] and not check_cell[sector][num]


def sudoku(grid):
    # finding empty space
    empty_space = find_empty_space(grid)
    if not empty_space:
        print_grid(grid)
        return True
    else:
        row, col = empty_space
        
    for i in range(1,10):
        # check if we can place any number
        if check_occupied(i, row, col):
            grid[row][col] = i
            check_row[row][i] = 1
            check_col[col][i] = 1
            sector = 3*(row//3) + (col//3)
            check_cell[sector][i] = 1
            
            if sudoku(grid):
                return True
            
            # unset/backtrack
            grid[row][col] = 0
            check_row[row][i] = 0
            check_col[col][i] = 0
            check_cell[sector][i] = 0
            
    return False
    
    
global check_row, check_col, check_cell, grid
check_row = [[0]*10 for _ in range(10)]
check_col = [[0]*10 for _ in range(10)]
check_cell = [[0]*10 for _ in range(10)]

grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
      [5, 2, 0, 0, 0, 0, 0, 0, 0],
      [0, 8, 7, 0, 0, 0, 0, 3, 1],
      [0, 0, 3, 0, 1, 0, 0, 8, 0],
      [9, 0, 0, 8, 6, 3, 0, 0, 5],
      [0, 5, 0, 0, 9, 0, 6, 0, 0],
      [1, 3, 0, 0, 0, 0, 2, 5, 0],
      [0, 0, 0, 0, 0, 0, 0, 7, 4],
      [0, 0, 5, 2, 0, 6, 3, 0, 0]]


for i in range(9):
    for j in range(9):
        num = grid[i][j]
        if num:
            check_row[i][num] = 1
            check_col[j][num] = 1
            sector = 3*(i//3) + (j//3)
            check_cell[sector][num] = 1


if not sudoku(grid):
    print("Solution not found")