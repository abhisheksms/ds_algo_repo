def min_platform(arr, dep, n):

    # inititlaized with 1 for the first arrival
    expected = max_platform = 0
    arr = sorted(arr)
    dep = sorted(dep)
    
    i = 0
    j = 0

    while i < n and j < n:
        if arr[i] <= dep[j]:
            expected += 1
            i += 1
            max_platform = max(max_platform, expected)
        else:
            expected -= 1
            j += 1
  
    return max_platform


print(min_platform([900,940,950,1100,1500,1800],[910, 1200, 1120, 1130, 1900, 2000],6))