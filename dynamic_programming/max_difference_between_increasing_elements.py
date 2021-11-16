class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        """
        -Initialize min_val to negative infinity
        -First find minimum of 2 mumbers
        -If number encountered is greater than minimum
        -then calculate diff with min_val and get maximum among them
        similar to best time to buy and sell stock(with minor diff)

        T.C - O(n)
        S.C - O(1)
        """
        res = -1
        min_val = float("inf")
        for index, num in enumerate(nums):
            min_val = min(num, min_val)
            if num > min_val:
                res = max(res, num-min_val)
                
        return res