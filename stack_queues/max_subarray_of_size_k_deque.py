class Solution:
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:
        """
        Time complexity O(n)
        Time complexity O(n)

        1. First element of deque must contain maximum value of the subarray
        2. We create Monotonic deque
        3. We create result of size n-k+1
        4. WE STORE INDEXES NOT VALUES
        
        """
        d = deque()
        res = []
        n = len(a)
        
        for i, val in enumerate(a):
            
            # pop elements outside the sliding window
            start = i - k + 1 # pain point
            while d and d[0] < start:
                d.popleft()
            
            while d and a[d[-1]] <= a[i]:
                d.pop()
            
            d.append(i)
            
            # pain point
            # if the iterator has crossed the window size
            if i >= k-1:
                res.append(a[d[0]])
            
            
        return res