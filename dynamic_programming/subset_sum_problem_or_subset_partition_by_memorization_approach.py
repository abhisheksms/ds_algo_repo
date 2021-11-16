from itertools import product
def findPartition(array, n): 
    """
    Q.  Can we repeat the numbers while making a sum?
    Q. Why or??
       Because we could also make the sum without using the 
       current element, represented by the row value
    1. If column number is less than array, we take the value of the row above
    - What is i and what is j???

    Divide sum by 2
    Do a knapsack on the array, and get it to this sum
    If so, then return True

    row: array elements
    col: The computed sum
    """
    col = sum(array)//2 + 1
    row = n+1
    dp = [[True]*col for _ in range(row)]
    
    for j in range(1, col):
        dp[0][j] = False
        
    
    for i,j in product(range(1, row), range(1, col)):
        if j < array[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j] or dp[i-1][j-array[i-1]]
    
    
    return dp[-1][-1]
    
array = [2,3,5,6] 
n = len(array) 
if findPartition(array, n) == True: 
    print("Can be divided into two subsets of equal sum") 
else: 
    print("Can not be divided into two subsets of equal sum") 