class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def is_equal(self, fa, fb):
        count = 0
        for x, y in zip(fa, fb):
            if x == y:
                count += 1

        return True if count == 26 else False

    def solve(self, A, B):
        """
        - If all characters in the window are also present in A, 
        then the window is a given permutation of A,  we can store it in a hash set

        - This problem appears to be a candidate of Rabin Karp algorithm

        - video explanation: 13:50, count variable, which determines by how many character is the string A differering from the substring
        - Sliding window, remove frequency of character from left, 
        if the frequency doesn't match, increase the count,else decrease if it matches
        add character to right, increase frequency of right character
        if the frequency matches decrease the count, else increase it
        - if the count is zero, increment the result

        - Alternatively match the 26 length frequency array after sliding the window each time
          It won't increase the complexity by much
        """
        fa = [0]*26
        fb = [0]*26

        for i, val in enumerate(A):
            fa[ord(val)%97] += 1

        head, tail, res = 0, 0, 0
        na, nb = len(A), len(B)

        # first window
        while tail < na:
            fb[ord(B[tail])%97] += 1
            tail += 1

        if self.is_equal(fa, fb):
            res += 1

        #subsequent windows
        while tail < nb:
            # add new tail char
            tail_val = ord(B[tail])%97
            fb[tail_val] += 1
            tail += 1

            # discard previous head char
            head_val = ord(B[head])%97
            fb[head_val] -= 1
            head += 1

            if self.is_equal(fa, fb):
                res += 1

        return res