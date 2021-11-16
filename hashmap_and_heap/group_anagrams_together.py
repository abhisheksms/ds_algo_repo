def get_unique_word(word):
    new_arr = [0]*26
    for w in word:
        ascii_val = ord(w)%97
        new_arr[ascii_val] += 1
        
    res = ""
    for index, val in enumerate(new_arr):
        if index >= 0:
            res += (chr(index+97)*val)
            
    return res

def groupAnagrams(words,result):
    hash_map = {}
    for word in words:
        new_word = get_unique_word(word)
        if new_word not in hash_map:
            hash_map[new_word] = 1
        else:
            hash_map[new_word] += 1
    
    print(hash_map.keys())

if __name__ == '__main__':
    result = []
    words = ["cat", "dog", "tac", "god", "act"]
    groupAnagrams(words,result)