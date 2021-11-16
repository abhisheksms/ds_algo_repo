def count_sort(s):
    count = [0]*52
    '''
    A-Z 65-90
    a-z 97-122
    '''
    for i in s:
        val = ord(i)
        if 65 <= val <= 90:
            count[val%65] += 1
        else:
            count[(val%97) + 26] += 1
            
            
    res = ""
    for i in range(26):
        res += (chr(i+65)*count[i])
        
    for j in range(26, 52):
        res += (chr(j+97-26)*count[j])
        
    return res

print(count_sort("aaBBCzz"))