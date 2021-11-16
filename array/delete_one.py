class Solution:
    # @param A : list of integers
    # @return an integer
    def gcd(self, a, b):
        if b == 0:
            return a
            
        return self.gcd(b, a%b)
        
    def solve(self, A):
        fgcd = [A[0]]
        bgcd = [A[-1]]
        n = len(A)
        for i in range(1, n):
            if i == 1:
                fgcd.append(self.gcd(A[i], A[i-1]))
                bgcd.append(self.gcd(A[~i], A[~(i-1)]))
            else:
                fgcd.append(self.gcd(A[i], fgcd[i-1]))
                bgcd.append(self.gcd(A[~i], bgcd[i-1]))
       
        bgcd = bgcd[::-1]

        print(A)
        
        print("Forward gcd")
        print(fgcd)

        print("Backward gcd")
        print(bgcd)
        
        res = -1
        for i in range(n):
            if i == 0:
                val = bgcd[i+1]
            elif i == n-1:
                val = fgcd[i-1]
            else:
                val = self.gcd(fgcd[i-1], bgcd[i+1])
            res = max(res, val)
            
        return res

s= Solution()
print(s.solve([12, 15, 18]))