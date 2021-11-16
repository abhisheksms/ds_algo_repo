class Solution:
	# @param A : string
	# @return an integer
	def lengthOfLongestSubstring(self, s):
        n = len(s)
        head = 0
        tail = 0
        res = 0

        visited = [0]*26

        while tail < n:
            # first grow tail
            tail_val = ord(s[tail])%97
            if visited[tail_val] <= 0:
                visited[tail_val] += 1
            else:
                while s[head] != s[tail] and tail < n:
                    head_val = ord(s[head])%97
                    visited[head_val] -= 1
                    head += 1 
                # the matching character will be removed as well
                # Eg: abca
                head+=1

            # calculate the result
            res = max(res, tail - head + 1)
            tail += 1 # tail is increased anyways

        return res


# more efficient code
# there is no need to iterate the head
# we can directly jump the head + 1
class Solution:
	# @param A : string
	# @return an integer
	def lengthOfLongestSubstring(self, s):
        """
            - Different from longest common substring
            s1 = "abcdef"
            s2 = "aednek"
            FinD COMMON among them
        - Conside 2 strings
            1. abca
            2. abcd

            head is 0, tail is 3 what will we do??

        - USING A HASHMAP AS key: character, value: index of the character
        - hashmap: key: the character element
                   value: LATEST index position of the element
        """
        n = len(s)
        head = 0
        tail = 0
        res = 0

        hmap = {}

        while tail < n:
            
            # if tail character found somewhere earlier
            # and the head is behind the already seen character
            if s[tail] in hmap and hmap[s[tail]] >=  head:
                # recompute head first
                # new head first character after already seen character
                head = hmap[s[tail]] + 1
            else:
                res = max(res, tail - head + 1)
                
            # now update hash map
            hmap[s[tail]] = tail
            tail += 1 # tail is increased anyways
            

        return res