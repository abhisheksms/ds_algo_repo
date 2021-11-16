class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        """
        Weakness: Struggling with off by 1 errors in sliding window and two pointers
        This is a classic 2 pointer solution, memorize the approach
        """
        n = len(A)
        head, tail = 0, 0
        total = 0
        
        while tail < n:
            # expand tail
            if total < B:
                total += A[tail] 
            
            # shrink head
            # loop won't be executed until condition is met
            # takes care of condition if we have increase
            # and delete for a single element
            while total > B:
                total -= A[head]
                head += 1
                
            tail += 1
            if total == B:
                return A[head:tail]
            
        return [-1]