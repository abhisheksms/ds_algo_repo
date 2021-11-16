class newNode:  
#ok for all test cases required  
    def __init__(self, data):  
        self.data = data  
        self.left = None
        self.right = None
        
class info:
    def __init__(self, size, min_val, max_val, is_bst):
        self.size = size
        self.min_val = min_val
        self.max_val = max_val
        self.is_bst = is_bst
        
res = 0    
def largestBST(root): 
    """
    Huh?
    ret.min = min(left.min, min(right.min, root.data))
    ret.max = max(right.max, max(left.max, root.data))
    
    DRY RUN THE CODE ONCE BEFORE MUGGING/COPYING IT

    1. Create a class with variables: min, max, size and is_bst
    2. if null root, return(0, float("inf"), float("-inf"), True)
       Null node/Single node is BST in itself
    3. We have to satisfy the property
       left.max_val < root.data < right.min_val
    4. recurse and return left and and right subtrees
    5. if the left subtree is a BST
       if the right subtree is a BSR
       and left.max < root.data < right.max
       return info(1+left.size+right.size, some_min_stuff, some_max_stuff, True)
    6. else
       return info(max(left.size, right.size), 0, 0, False)
    """
    global res
    if root is None:
        # Huh???????????????????
        return info(0, float("inf"), float("-inf"), True)
    
    # if root.left is None and root.right is None:
    #     return info(1, root.data, root.data, True)
    
    left = largestBST(root.left)
    right = largestBST(root.right)
    
    ret = info(max(left.size, right.size),0,0,False)
    
    
    if left.is_bst and right.is_bst and left.max_val < root.data < right.min_val:
        ret.is_bst = True
        ret.min_val = min(root.data, min(right.min_val, left.min_val))
        ret.max_val = max(root.data, max(left.max_val, right.max_val))
        ret.size = 1 + left.size + right.size
        res = max(res, ret.size)
        
    return ret 
      

root = newNode(60)  
root.left = newNode(65)  
root.right = newNode(70)  
root.left.left = newNode(50) 
actual = largestBST(root)
print(res)

root = newNode(5)  
root.left = newNode(2)  
root.right = newNode(4)  
root.left.left = newNode(1)
root.left.right = newNode(3)  
actual = largestBST(root)
print(res)
