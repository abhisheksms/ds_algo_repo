class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        What is the MAXIMUM I CAN JUMP in each jump
        Remember this: i + nums[i]
        """
        left, right = 0, 0 # Here we are starting from absolute zero
        jumps = 0
        
        while right < len(nums)-1:
            # will return 0 if nums[0] is 0
            jumps += 1
            max_jump = max([i+nums[i] for i in range(left, right+1)])
            left, right = right+1, max_jump
        
        return jumps

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1 or nums[0] == 0: # hence adding this condition
            return 0
        left, right = 0, nums[0] # Here we are already doing the first jump
        jumps = 1
        
        while right < len(nums)-1:
            jumps += 1
            max_jump = max([i+nums[i] for i in range(left, right+1)])
            # max_jump already has i+nums[i]
            left, right = right+1, max_jump
        
        return jumps



#####################
# Identifying pain points
class Solution:
    def jump(self, nums: List[int]) -> int:
        left, right, jumps = 0,0,0 #pain point
        while right < len(nums) - 1: #pain point
            jumps+= 1
            max_jump = max([i+nums[i] for i in range(left, right+1)])
            left, right = right+1, max_jump #pain point
        
        return jumps
        
    
    
    