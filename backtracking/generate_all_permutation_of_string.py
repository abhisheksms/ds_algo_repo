def generate_permutation(A, start, end):
    """
    T.C. = O(N*N!)
    N to print array
    N! or (N-1!) to perform backtracking
    S.C. = O(1)
    """
    if start == end:
        print(A)
        
    for index in range(start, end+1):
        A[index], A[start] = A[start], A[index]
        generate_permutation(s, start+1, end)
        # backtracking
        # it is needed if we use the string as a global varaible
        A[index], A[start] = A[start], A[index]

s = ["A", "B", "C"]
print(generate_permutation(s, 0, len(s)-1))