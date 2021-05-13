import random
a = [54, 26, 17, 93, 77, 31, 44, 20, 55]
def partition(low, high):
    # select random pivot and place at the end
    pivot = random.randint(low, high)
    a[pivot], a[high] = a[high], a[pivot]

    final_pos = low

    while low < high:
        if a[low] < a[high]:
            a[final_pos], a[low] = a[low], a[final_pos]
            final_pos += 1
        low+=1

    a[final_pos], a[high] = a[high], a[final_pos]

    return final_pos

def quickselect(low, high, k):
    #if a:
    val = partition(low, high)
    print(val)
    if val < k:
        # recurse right side
        print("Right")
        return quickselect(val+1, high, k)
    elif val > k:
        # recurse left side
        print("Left")
        return quickselect(low, val-1, k)
    else:
        return a[val]


print(quickselect(0, 8, 2))
