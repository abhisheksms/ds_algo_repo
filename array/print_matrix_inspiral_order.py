def spiral(R, C, m):
    """
    a: col start 
    b: col end

    c: row start
    d: row end
    """
    res = []
    a = c = 0
    b = d = R - 1

    while a < b and c < d:

        res.extend(m[c][i] for i in range(a, b))
        a+=1
        
        res.extend(m[j][b] for j in range(c, d))
        c+=1
        
        res.extend(m[d][i] for i in range(b, a-1, -1))
        b-=1

        res.extend(m[j][a-1] for j in range(d, c-1, -1))
        d-=1


    return res
    
matrix = [
     [1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16],
]
print(spiral(4,4,matrix))