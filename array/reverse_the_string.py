class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        """ 
        In: "the sky is blue"
        Out: "blue is sky the"
        """
        A = A.strip()
        A = A.split()
        A= A[::-1]
        return " ".join(A)