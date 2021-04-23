def sort_arr(a):
    # edge cases

    if len(a) == 1:
        return a

    if a == []:
        return []

    n = len(a)
    zero_index = 0
    two_index = n - 1

    pivot = 0
    while zero_index < two_index:

        if a[pivot] == 2:
            a[pivot], a[two_index] = a[two_index], a[pivot]
            two_index -= 1
        elif a[pivot] == 0:
            a[pivot], a[zero_index] = a[zero_index], a[pivot]
            zero_index += 1
            # only diff
            pivot += 1
        else:
            pivot += 1 

    return a


print(sort_arr([2, 0, 1]))
print(sort_arr([2,2,2,0,0,0,0,1,1,1]))
print(sort_arr([2, 2, 0, 0]))