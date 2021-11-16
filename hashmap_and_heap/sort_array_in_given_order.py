class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        """
        Too many edge cases

        Requires 2 hash_map
        one to keep track of whether the elements of array A is visited or not
        other to check the the value: list of indexes mapping

        Understand the problem properly
        """
        res = []
        done = [0]*len(A)
        A.sort()
        
        hmap = {}
        for i, val in enumerate(A):
            if val in hmap:
                hmap[val].append(i)
            else:
                hmap[val] = [i]
        
        
        for i in B:
            if i in hmap:
                for z in hmap[i]:
                    res.append(A[z])
                    done[z] = 1
                                       
        for i, val in enumerate(done):
            if val == 0:
                res.append(A[i])
        
        return res