class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        """
        ASK YOURSELF WHY DID WE NEED TO COMPUTE THE PREFIX BETWEEN
        THE ARRAYS????
        No need to compute difference between prefixes
        check the prefix for duplicate or zero values
        """
        n = len(A)
        prefix = [0]*n
        res = 0
        
        for index, val in enumerate(A):
            res+=val
            prefix[index] = res
            
        hash_set = set()
        for i in prefix:
            if i == 0 or i in hash_set:
                return 1
            hash_set.add(i)
                
        return 0
            
    
    
s=Solution()
print(s.solve([-1,1]))
print(s.solve([3,-1,1]))
print(s.solve([1,-3,2,84]))
print(s.solve([1,2,3]))