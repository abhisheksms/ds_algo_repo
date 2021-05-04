def rotate(R,C,m):
    # rotation is only possible in a square matrix
    
    # clockwise
    for i in range(R):
        for j in range(i+1):
            m[i][j], m[j][i] = m[j][i], m[i][j]

    for i in range(R):
        for j in range(C//2):
            # ~j == C-j-1
            m[i][j], m[i][~j] = m[i][~j], m[i][j]

    # anticlockwise transpose along the secondary diagonal(antidiagonal) 
    # and reverse by column

    return m


matrix = [
     [1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16],
]
print(rotate(4,4,matrix))