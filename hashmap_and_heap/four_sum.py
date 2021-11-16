from collections import namedtuple  
pair = namedtuple('pair',['x','y'])


def fourSum (array, n, result):
    """
    Convert the integer to string array to simplitfy the problem slightly
    
    Possible knapsack as well
    - One approach, merge_sort + binary search
    - Hashmap: key = sum 
             value = list of array index objects
             all four index must be unique
    """
    hash_map = {}
    for i in range(n-1):
        for j in range(i+1, n):
            val = array[i] + array[j]
            
            # exercise: use setdefault later
            if val not in hash_map:
                hash_map[val] = [pair(array[i], array[j])]
            else:
                hash_map[val].append(pair(array[i], array[j]))
                
                
            if result-val in hash_map:
                for p in hash_map[result-val]:
                    if (p.x != array[i] and p.y != array[j]) \
                    and (p.x != array[i] and p.y != array[j]):
                        print(array[i], array[j], p.x, p.y)
    
    
array = [1, 5, 1, 0, 6, 0] 
n = len(array) 
# result = []
fourSum(array, n, 11) 
# print(result)