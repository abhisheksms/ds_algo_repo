class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        hash_set = set()
        res = 0

        point = namedtuple('point', ['x', 'y'])
        for i, j in zip(A,B):
            hash_set.add("i#j")

        for a in hash_set:
            for b in hash_set:
                if a != b and  (a[0] != b[0] and a[-1] != b[-1]):
                    c = "{}#{}".format(a[0], b[-1])
                    d = "{}#{}".format(b[0], a[-1])
                    if c in hash_set and d in hash_set:
                        res += 1

        return res//4