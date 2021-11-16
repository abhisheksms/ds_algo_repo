def pow(x, n):
    if n == 0:
        return 1
    
    if n % 2 == 0:
        return pow(x*x, n//2)
    else:
        return x*pow(x, n-1)

print(pow(2, 9))