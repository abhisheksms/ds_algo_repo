def distinct_elements(a, k, n):
    hash_map = {}
    unique_elem =start = end = 0
    res = []

    # build initial window
    while end < k:
        if a[end] not in hash_map:
            hash_map[a[end]] = 1
            unique_elem += 1
        else:
            hash_map[a[end]] += 1

        end+=1

    res.append(unique_elem)

    # slide window
    while end < n:
        if a[end] not in hash_map:
            hash_map[a[end]] = 1
            unique_elem += 1
        elif hash_map[a[end]] == 0:
            hash_map[a[end]] = 1
            unique_elem += 1
        else:
            hash_map[a[end]] += 1

        end+=1

        hash_map[a[start]] -= 1
        if hash_map[a[start]] == 0:
            unique_elem -= 1

        start += 1

        res.append(unique_elem)

    return res


print(distinct_elements([2,3,2,4,5,3,3,4], 3, 8))

print(distinct_elements([1,2,1,3,4,2,3], 4, 7))