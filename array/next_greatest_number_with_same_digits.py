def next_greatest_number(n):
    a = list(map(int, f"{n}"))
    
    # start from th last index
    len_arr = len(a)
    i = len_arr - 1

    # stop if i-1 is smaller than i
    while a[i-1] > a[i]:
        i-=1

    if i == 0:
        return -1
    else:
        next_greatest_index = i
        # from i get the next largest number to val
        for j in range(i+1, len_arr):
            if a[i-1] < a[j] < a[next_greatest_index]:
                next_greatest_index = j

        # swap i-1 with next largest number
        a[i-1], a[next_greatest_index] = a[next_greatest_index], a[i-1]

    # sort the remainindex after i-1
    a[i:] = sorted(a[i:])

    return int(''.join(map(str, a)))


print(next_greatest_number(218765))
print(next_greatest_number(54321))