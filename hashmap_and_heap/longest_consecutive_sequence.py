class Solution:
	# @param A : tuple of integers
	# @return an integer
	def longestConsecutive(self, A):
	    """
	    1. store all elements in a map
	    2. for a given element i check
	       if i-1 not in map
	         create a while loop until i+1 in map
	           and update map
	       else
	          continue
	          
	    TC O(n)
	    SC O(n)
	           
	     
	    """
	    res = 0
	    
	    hash_set = set(A)
	    for i in hash_set:
	        temp = 0
	        if i-1 not in hash_set:
	            temp = 1
	            while i+1 in hash_set:
	                i += 1
	                temp += 1
	                
	        res = max(res, temp)
	    
	    return res