import math
def find_two_distinct_elem(a):
    init_xor = 0
    for elem in a:
        init_xor ^= elem

    
    # bit_val = init_xor & ~(init_xor - 1)
    # most_significant_bit = int(math.log2(bit_val))

    #bit_val = init_xor & ~(init_xor - 1)
    most_significant_bit = int(math.log2(init_xor & -init_xor))

    res_1 = res_0 = 0

    for index, num in enumerate(a):
        if num & (1<<most_significant_bit) == 0:
            res_0 ^= num
        else:
            res_1 ^= num

    return res_1, res_0


print(find_two_distinct_elem([2,4,7,9,2,4]))