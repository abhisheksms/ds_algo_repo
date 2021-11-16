from collections import Counter
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        mod = 10**9 + 7

        res = 0
        map_x = Counter(A)
        map_y = Counter(B)

        for i, j in zip(A, B):
            res += (map_x[i]-1) * (map_y[j]-1)
            res %= mod

        return res % mod