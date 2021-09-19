def areParanthesisBalanced(expr) : 
    stack = [] 
    # odd length stack
    if len(expr) % 2 == 1:
        return False
    #Write Your Code here
    for ch in expr:
        if ch == '(':
            stack.append(')')
        elif ch == '{':
            stack.append('}')
        elif ch == '[':
            stack.append(']')
        elif stack.pop() != ch:
            return False

    # if stack still not empty   
    if len(stack):
        return False
        
    return True

print(areParanthesisBalanced("{()}[]"))
print(areParanthesisBalanced("{(){[]"))