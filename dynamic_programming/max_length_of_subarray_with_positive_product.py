class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        """ 
        Can be used for max length subarray with both positive and negative product
        pos, neg store the positive and negative elements for the PREVIOUS ELEMENT
        
        Your believes are SHIT
        
        if nums[i] > 0 
            pos = 1 + pos
            neg = 1 + neg if neg > 0 else 0
        
        if nums[i] < 0
           # SWAPPPP
           pos, neg = 1 + neg if neg > 0 else 0, 1 + pos
           
        """
        pos, neg, res= 0, 0, 0  
            
        for i in range(len(nums)):
            if nums[i] > 0:
                pos += 1
                
                # no new negative if previous negative iz zero
                neg = neg + 1 if neg > 0 else 0
            elif nums[i] < 0:
                #SWAPP
                
                # no new positive as well if previous negative iz zero
                pos, neg = neg + 1 if neg > 0 else 0, pos + 1
                
            else:
                pos, neg = 0, 0
                
            res = max(pos, res)
            
        return res