import functools
from math import log10

def get_palindrome(a, odd=False):
    if odd:
        mid_elem = a[-1]
        prefix = a[:-1]
        res = prefix + mid_elem + prefix[::-1]
    else:
        res = a + a[::-1]

    return int("".join(map(str, res)))


def closest_palindrome(val):
    a = list(map(int, f"{val}"))
    n = len(a)
    # edge cases

    # 10, 100, 1000
    if log10(val).is_integer():
        return val - 1
    
    # 99, 999, 999
    if log10(val+1).is_integer():
        return val + 2

    # 101, 1001
    if log10(val-1).is_integer():
        return val - 2

    # # 50, 20, 300
    # if val%10 == 0:
    #     for i in range(len(a)//2):
    #         a[~i] = a[i]
        
    #     return a
    
    if n%2 != 0:
        odd_prefix = int("".join(map(str,a[:n//2+1])))
        low_val = get_palindrome(f"{odd_prefix-1}", odd=True)
        mid_val = get_palindrome(f"{odd_prefix}", odd=True)
        high_val = get_palindrome(f"{odd_prefix+1}", odd=True)
    else:
        prefix = int("".join(map(str,a[:n//2])))
        low_val = get_palindrome(f"{prefix-1}")
        mid_val = get_palindrome(f"{prefix}")
        high_val = get_palindrome(f"{prefix+1}")


    min_diff = float("inf")
    res = 0
    for i in [low_val, mid_val, high_val]:
        diff = abs(i-val)
        if diff < min_diff:
            min_diff = diff
            res = i

    return res


print(closest_palindrome(832))
print(closest_palindrome(1000))
print(closest_palindrome(12321))
print(closest_palindrome(123321))
print(closest_palindrome(50000))