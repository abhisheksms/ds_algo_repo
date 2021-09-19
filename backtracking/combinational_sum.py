global res_list
res_list = []
import time
start_time = time.time()
def combinational_sum(A, res, res_sum, actual_res):
    if res_sum == actual_res:
        temp = sorted(res)
        if temp not in res_list:
            res_list.append(temp)
            print(res)
    
    for i in range(0, len(A)):
        if res_sum + A[i] <= actual_res:
            res.append(A[i])
            combinational_sum(A, res, res_sum + A[i], actual_res)
            res.pop()
        else:
            return
    

A = [1,2,3]
combinational_sum(A, [], 0, 4)
print(f"Time taken {time.time() - start_time} seconds")