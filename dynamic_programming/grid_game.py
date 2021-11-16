class Solution:
    def gridGame(self, grid: List[List[int]]) -> int: 
        """
        -precalculate top row sum
        -remove ith elem from top row
        -calculate result: max of top sum, bottomsum and minimum of this result
        -add ith elem to bottom row

        T.C - O(n)
        S.C - O(1)
        """
        res = math.inf
        topsum = sum(grid[0])
        bottomsum = 0
        for i in range(len(grid[0])):
            # takes care of intitial case of only using topsum excluding first elem
            topsum -= grid[0][i]
            
            #THIS IS A GAME
            #FIRST BOT WANTS TO MIMIMIZE GAINS OF SECOND BOT
            #SECOND BOT WANTS TO MAXIMIZE "available" gains
            #max(topsum, bottomsum) second robot
            #min(res, above_val) first robot
            """
            min(
                max(0, bottomsum[1:n-1]),
                max(topsum[n-1:n], bottomsum[2:n-1]),
                max(topsum[n-2:n], bottomsum[3:n-1]),
                ...
                max(topsum[1:n], 0)
            )
            
            """
            res = min(res, max(topsum, bottomsum))
            # takes care of final case of only using bottom excluding last elem
            bottomsum += grid[1][i]
            
        return res