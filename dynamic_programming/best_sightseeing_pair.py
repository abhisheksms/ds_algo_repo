class Solution:
    def maxScoreSightseeingPair(self, A):
        """
        Our approach
        Get max 2 elements, update for every new element(greedy)
        
        Break it down
        We want to get max(A[i] + i    +    A[j]-j)
        """
        # Inititalize values
        prev_max = A[0] + 0
        res = A[0] + 0 + A[1] - 1
        for j in range(1, len(A)):
            res = max(prev_max + A[j]-j, res)
            prev_max = max(prev_max, A[j]+j)
            
        return res