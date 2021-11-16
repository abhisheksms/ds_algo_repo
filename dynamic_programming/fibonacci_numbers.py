class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        a, b = 0, 1
        i = 2
        while i <= n:
            c = a + b
            a = b
            b = c
            
            i += 1
            
        return c
        