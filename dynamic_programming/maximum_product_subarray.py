class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """ 
        Thinking in terms of single edge case instead of global thinking
        
        First, if there's no zero in the array, then the subarray with  
        maximum product must start with the first element or end with the
        last element. And therefore, the maximum product must be some 
        prefix product or suffix product. 
        """
        res, prefix, suffix, n = float("-inf"), 0, 0, len(nums)
        for i in range(n):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[~i]
            res = max(res, prefix, suffix)
        
        return res



class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """ 
        Since we observed that negative values can produce the maximum      
        product, 
        WE KEEP TRAKC OF BOTH maximum product and the minimum product. 
        The minimum product, when multiplied by another negative number, 
        can produce a possible answer

        In this case, we observe that we only ever need to keep track 
        of the subproblem solution IMMEDIATELY PRECEDING our current 
        subproblem
        
        Hence we can avoid allocating an array, and improve the space 
        complexity from ~O(N) to ~O(1)
        """
        # I have seen the problem, yet I am blank
        min_val, max_val, res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            temp_min, temp_max = min_val, max_val
            max_val = max(nums[i]*temp_max, nums[i]*temp_min, nums[i])
            min_val = min(nums[i]*temp_max, nums[i]*temp_min, nums[i]) # get min_val for next iteration
            res = max(res, max_val)
            
        return res