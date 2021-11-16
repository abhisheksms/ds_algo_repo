class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        """
        compute a prefix multiplication
        we add 1 initially to the prefix at the start

        # i goes from 0 to len(s)
        # j goes from i+1 to len(s)+1
        """

        s = str(A)
        prefix = [1]*(len(s)+1)
        res = 1
        for index, val in enumerate(s):
            res*=int(val)
            prefix[index+1] = res
        
        hash_set = set()
            
        
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                val = prefix[j]//prefix[i]

                if val in hash_set:
                    return 0
                else:
                    hash_set.add(val)
    
        return 1