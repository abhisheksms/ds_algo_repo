def maxSumSubseq(A, i, n, prev=float('-inf')):
    """
    res = max(M[i-1], a[i]+M[i-2])
    """
    prev_max1, prev_max2 = A[0], 0
    for i in range(1, n):
        prev_max1, prev_max2 = max(prev_max1, A[i]+prev_max2), prev_max1
    
    return prev_max1


if __name__ == '__main__':

	A = [5, 20, 15, -2, 18]
	print("Maximum sum is", maxSumSubseq(A, 0, len(A)))