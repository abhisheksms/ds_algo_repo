def multiplicative_inverse(a,mod):
    """
    We are using fermat's little theorem
    Only works when mod is prime
    """
    b = mod - 2
    res = 1
    
    # a**b % mod
    while b > 0:
        if b%2 == 0:
            a = (a*a) % mod
            b //= 2
        else:
            res = (res*a) % mod
            b -= 1
    
    return res
    

print(multiplicative_inverse(3,11))