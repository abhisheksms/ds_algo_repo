global N
N = 2
def combination_parantheses(s, index, open_count, close_count):
    if close_count == N :
        print(s)
        return
    else:
        # if open greater than close
        if open_count > close_count:
            s[index] = "}"
            combination_parantheses(s, index+1, open_count, close_count+1)
            
        if open_count < N:
            s[index] = "{"
            combination_parantheses(s, index+1, open_count+1, close_count)

s = [" "] * 2 * N
index = 0
open_count = 0
close_count = 0
combination_parantheses(s, index, open_count, close_count)