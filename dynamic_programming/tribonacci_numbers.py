class Solution:
    def tribonacci(self, n: int) -> int:
        """
        We can also use matrix exponential
        https://leetcode.com/problems/n-th-tribonacci-number/discuss/1482728/C%2B%2BPython-2-solutions%3A-DP-Matrix-exponential-Picture-explained-Clean-and-Concise
        """
        if n <= 1:
            return n
        if n == 2:
            return 1
        
        a, b, c, i = 0, 1, 1, 3
        while i <= n:
            d = a + b + c
            a = b
            b = c
            c = d
            i += 1
            
        return c
    
    # better approach
    def tribonacci(self, n):
        a, b, c = 1, 0, 0
        for _ in range(n):
            a, b, c = b, c, a + b + c
               
        return c

        