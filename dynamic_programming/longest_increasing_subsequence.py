# from typing import List
# class Solution:
#     def lengthOfLIS(self, a: List[int]) -> int:
#         n = len(a)
#         if n == 1:
#             return 1

#         lis = [1]*n
#         max_lis = 1

#         for i in range(1, n):
#             if a[i] > a[i-1]:
#                 lis[i] = max(1+lis[i-1], max_lis)
#             else:
#                 lis[i] = lis[i-1]

#             max_lis = max(lis[i], max_lis)

#         return max_lis

from typing import List
class Solution:
    def lengthOfLIS(self, a: List[int]) -> int:
        n = len(a)
        if n == 1:
            return 1

        lis = [1]*n
        max_lis = 1

        for j in range(1, n):
            for i in range(j):
                if a[i] < a[j]:
                    lis[j] =  max(1+lis[i], lis[j])
                    
        max_lis = max(lis)

        return max_lis

s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(s.lengthOfLIS([0,1,0,3,2,3]))#4
print(s.lengthOfLIS([7,7,7,7,7]))#1


##################3
print(s.lengthOfLIS([4,10,4,3,8,9]))#3
print("algo")
print(s.lengthOfLIS([5,2,8,6,3,6,9,7]))#4