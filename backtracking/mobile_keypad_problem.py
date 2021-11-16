hash_table = ["", "", "abc", "def", "ghi", "jkl",  
                    "mno", "pqrs", "tuv", "wxyz"] 

def mobile_keypad(in_str, index, out_str):
    if index == len(in_str):
        print(out_str)
        return 
    
    str_range = hash_table[int(in_str[index])]
    # looping over the range
    for i in range(len(str_range)):
        out_str += str_range[i]
        mobile_keypad(in_str, index+1, out_str)
        out_str = out_str[:-1]


mobile_keypad("45", 0, "")