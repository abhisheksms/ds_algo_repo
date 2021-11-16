def print_number_ascending(A, i):
    if i == -1:
        return
    print_number_ascending(A, i-1) 
    print(A[i])

def print_number_descending(A, i):
    if i == -1:
        return

    print(A[i])
    print_number_descending(A, i-1)
    


a = [i for i in range(5)]
print_number_ascending(a, len(a)-1)
print("*" * 10)
print_number_descending(a, len(a)-1)
