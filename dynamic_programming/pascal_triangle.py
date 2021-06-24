from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        rowIndex += 1

        res = [1]*rowIndex
        for i in range(1, rowIndex):
            for j in range(i-1, 0, -1):
                res[j] = res[j-1] + res[j]


        return res


s = Solution()
print(s.getRow(3))
print(s.getRow(4))
print(s.getRow(5))
print(s.getRow(6))