from collections import Counter

def print_string(a, head, tail):
    print(a[head: tail+1])

def get_next_candidate(head, tail, a, b, hash_map): 
    """

    - similar to min window substring
   - 2 pointer + sliding window + hash map 
   - increase tail
     then increase head
      i.e. see if we can increase head, without losing any important character
   - n iterations of increasing head
   - n iterations of increasing tail
     hence time complexity is linear
   - WE HAVE A total variable which stores count of B 
     Hence if total == len(B)
     we know we have candidate
     no need to traverse the hash_map to check if freq[] of all chars is zero

   - Core Problem: Finding the valid candidates, by increasing head and tail
   - histogram sweep?

   - Find first window
   - Delete one character from left
   - Move right until right hapeens to be the deleted character
   - Now increase left(trim) until

    """   
    # increase tail until we reach deleted character
    tail += 1
    while True:
        if a[tail] in hash_map:
            hash_map[a[tail]] -= 1
        if a[head] == a[tail]:
            break
        tail += 1
        
    # trim characters from left
    # until hash_map[ch] <= 0
    while head < tail:
        if a[head] in hash_map and hash_map[a[head]] == 0:
            break 
        elif a[head] in hash_map:
            hash_map[a[head]] += 1
        head += 1
        
    print(hash_map)
    print_string(a, head, tail)

    return head, tail, a, b, hash_map
    

def get_valid_candidates(a, b):
    """
    increase head, increment hash_map values
    increase tail, decrement hash_map values
    """
    hash_map = Counter(b)
    head = 0
    tail = 0
    total = 0
    
    # get first window
    while True:
        if a[tail] in hash_map:
            total += 1
            hash_map[a[tail]] -= 1
        if total == len(b):
            break
        tail += 1
    
    print(hash_map)
    print_string(a, head, tail)
    print(f"head: {head}, tail: {tail}")
    
    while tail < (len(a) - 1):
        head, tail, a, b, hash_map = get_next_candidate(head, tail, a, b, hash_map)
        print(f"head: {head}, tail: {tail}")
    
    

A = "ADOBECODEBANC"
B = "ABC"
get_valid_candidates(A, B)