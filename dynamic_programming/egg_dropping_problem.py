# class Solution:
#     def egg_drop(self, dp, e: int, f: int):
#         if f==0 or f==1:
#             return f

#         if e==1:
#             return f

#         if dp[e][f] != -1:
#             print(dp)
#             return dp[e][f]

#         min_val = float("inf")

#         for k in range(e, f+1):

#             #find minimum number of attempts
#             # in the WORST CASE(hence using max)
#             temp = 1 + max(self.egg_drop(dp, e-1, f-1), self.egg_drop(dp, e, f-k))
#             min_val = min(min_val, temp)

#         dp[e][f] = min_val
#         return dp[e][f]

    
#     def superEggDrop(self, e: int, f: int) -> int:
#         dp = [[-1]*(f+1) for _ in range(e+1)]

#         return self.egg_drop(dp, e, f)


# s = Solution()
# print(s.superEggDrop(3, 14))
# # print(s.superEggDrop(1, 2))
# # print(s.superEggDrop(2, 6))


INT_MAX = 32767

def eggDropProblem(n, k): 
    
    matrix = [[0 for x in range(k + 1)] for x in range(n + 1)] 
    
    for i in range(1, n + 1): 
        matrix[i][1] = 1
        matrix[i][0] = 0
    
    for j in range(1, k + 1): 
        matrix[1][j] = j 
    
    for i in range(2, n + 1): 
        for j in range(2, k + 1): 
            matrix[i][j] = INT_MAX 
            for x in range(1, j + 1): 
                res = 1 + max(matrix[i-1][x-1], matrix[i][j-x]) 

                matrix[i][j] = min(matrix[i][j], res)
                
    
    for m in matrix:
        print(m, end = "\n")
    print()

    return matrix[n][k] 
  
# n = 2
# k = 36
n = 2 #eggs
k = 6 #floors
print("Minimum trails " + str(n) + " eggs and " 
       + str(k) + " floors is " + str(eggDropProblem(n, k))) 

