class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        What is the max index that can be reached so far from current index?
        if the current index is greater than max_index, return False
        Eg: [3,2,1,0,4], i = 5 , m = 3
        Remember this: i+nums[i]
        """
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            # possible max index from current index
            m = max(m, i+n)
            
        return True