# our approach
def find_celeb(a, n):
    potential_candidates = [i if a[0][i]==1 else -1 for i in range(n)]
    for candidate_index, num in enumerate(potential_candidates):
        if num != -1:
            count_1 = 0
            for i in range(n):
                if a[candidate_index][i] == 0:
                    potential_candidates[i] = -1
                else:
                    count_1 += 1

            if count_1 == 0:
                return candidate_index

    return -1

# solution
def find_celebrity(a, n):
    x, y = 0, n-1

    while x < y:
        if a[x][y]:
            # x knows y, x is not celebrity
            x += 1
        else:
            # x does not know y, y is not celebrity
            y -= 1

    for i in range(n):
        if a[x][i]:
            # the element consider also knows someone hence 
            # not a celebrity
            return -1

    return x


matrix = [
     [1,1,1,1],
     [0,0,1,1],
     [0,0,0,1],
     [0,0,0,0],
]

print(find_celebrity(matrix, 4)) #3