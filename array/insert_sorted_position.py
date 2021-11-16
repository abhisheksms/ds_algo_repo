# insert an element in a sorted array and return the position
def insert_sorted_pos(arr, elem):
    """
    using a while loop instead of recursion

    only right half executed for single element
    hence we return low

    At the time of returning
    low will be low 
    high will be low - 1
    """
    low = 0
    high = len(arr) - 1

    # = if there is just a single element
    while low <= high:
        mid = (low + high) // 2
        if elem < arr[mid]:
            high = mid - 1 # left half
        else:
            low = mid + 1 # right half
    
    print(f"low {low}, high {high}")
    return low # how do we end it??

print(insert_sorted_pos([1, 2, 3, 4, 5], 6))


print(insert_sorted_pos([], 1)) #done
print(insert_sorted_pos([1], 1)) #done
print(insert_sorted_pos([3,3,3], 3))
print(insert_sorted_pos([1,2,5], 3))