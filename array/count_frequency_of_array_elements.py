from collections import Counter
def count_freq(a):
    n = len(a)
    
    for i in range(n):
        # decrement current number
        a[i] -= 1

        # get the actual value
        val = a[i] % 7
        
        # add the required value within the array
        a[val] += 7

    
    return {i+1: a[i]//7 for i in range(n)}

print(count_freq([5,2,7,7,5,5,2]))