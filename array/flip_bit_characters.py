def flip_bit_characters(ar):
    cur = 0
    res = 0
    l = 0
    r = 0
    ans = [-1,-1]
    for i in range(len(ar)):
        if ar[i] == "0":
            cur+=1
        else:
            cur-=1
            
        #res = max(cur, res)
        if res < cur:
            ans[0] = l+1
            ans[1] = r+1
            res = cur
        
        # start afresh
        if cur < 0:
            cur = 0
            l=i+1
            r=i+1
        else:
            r+=1
        
    if ans[0] == -1:
        return []
    else:
        return ans
        

print(flip_bit_characters("010")) #[]