#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countOfPermutation' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING a as parameter.
#
# global count
# count = 0

class Solution:
    def __init__(self):
        self.count = 0

    def get_count(self, A, start, end, index):
        if start == end:
            self.count += 1
            return
        
        for index in range(start, end+1):
            A[index], A[start] = A[start], A[index]
            self.get_count(A, start+1, end, index)
            A[index], A[start] = A[start], A[index]

    def get_res(self):
        return self.count


def countOfPermutation(a):
    n = len(a)
    ar_list = list(a)
    start = 0
    end = n-1
    index = 0
    s = Solution()
    s.get_count(ar_list, start, end, index)
    return s.get_res()

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     a = input()

#     result = countOfPermutation(a)

#     fptr.write(str(result) + '\n')

#     fptr.close()

print(countOfPermutation("abc"))
