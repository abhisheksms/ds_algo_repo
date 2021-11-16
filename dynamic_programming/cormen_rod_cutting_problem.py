import time
start_time = time.time()
# def cut_rod(p, n):
#     if n == 0:
#         return 0

#     q = float("-inf")
#     for i in range(n):
#         q = max(q, p[i] + cut_rod(p, n-i))

#     return q
# ctr = 0
# def memo_cut_rod(p, n, r):
#     # global ctr
#     # ctr += 1
#     # print(ctr)
    
#     if r[n] >= 0:
#         return r[n]

#     if n == 0:
#         q = 0
#     else:
#         q = float("-inf")
#         for i in range(1,n+1):
#             q = max(q, p[i] + memo_cut_rod(p, n-i, r))
            
#     r[n] = q
#     print(r)
#     return q


# def cut_rod(p, n):
#     r = [float("-inf") for i in range(n)]
#     return memo_cut_rod(p, n-1, r) # since r[n] would give KeyError

def cut_rod(p, n):
    r = [0] * (n+1)
    r[0] = 0
    for j in range(1, n+1):
        q = float("-inf")
        for i in range(1, j+1):
            q = max(q, p[i] + r[j-i])

        r[j] = q

    print(r)
    return r[-1]



prices = [1,5,8,9]
print("result is")
print(cut_rod([0,1,5,8,9], 4))
print(cut_rod([0,1,5,8,9,10,17,17,20], 8))

print(f"time taken {time.time() - start_time} seconds")