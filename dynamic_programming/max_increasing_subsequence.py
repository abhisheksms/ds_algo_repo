def IncreasingSum(arr, n): 
    """
    - Store a copy of original array
    - Compare 2 indexes i, j
    - if a[j] is less than a[i]
      then store max of c[i] and c[j]+a[i]
    - Key Learnings: 
      STORE THE RESULT IN A SEPARATE ARRAY AT SAME INDEX
      IF VALUE AT J IS SMALLER THAN VALUE AT I
    """
    #Write your code here 
    c = arr.copy()
    for i in range(1, n):
        j = 0
        while j < i:
            if arr[j] <= arr[i]:
                c[i] = max(c[i], c[j]+arr[i])
            j += 1
        
    return max(c)
  
# Driver Code 
arr = [1, 101, 2, 3, 100, 4, 5] 
n = len(arr) 
print("Sum of maximum sum increasing " + 
                     "subsequence is " +
                  str(IncreasingSum(arr, n))) 