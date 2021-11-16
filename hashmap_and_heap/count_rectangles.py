class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        """
        store A, B comnination in hashset
        for a given pair (A1, B1) and (A2, B2)
        check if (A1, B2) and (A2, B1) exist or not

        before making the check ensure both points are not the same
        """
