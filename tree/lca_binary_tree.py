import sys
class Node: 
    def __init__(self, key): 
        self.key = key  
        self.left = None
        self.right = None

        
#ok for all test cases required  
def findLCA(root, n1, n2): 
    """
    1. if root is None return 0
    2. if value in n1, n2 return value
    3. find left and right
    4. if left >0 and right >0 , we found the value, exit
    5. Now, we return left or right if any one is greater than zero
       else return 0
    6. WE ONLY RETURN/PROPAGATE n1 or n2 upwards or we return 0
    """
    if root is None:
        return 0
    
    if root.key in (n1, n2):
        return root.key
    
    left = findLCA(root.left, n1, n2)
    right = findLCA(root.right, n1, n2)
    
    if left > 0 and right > 0:
        print(root.key)
        sys.exit(0)
        
    if left > 0:
        return left
    elif right > 0:
        return right
    else:
        return 0

    
root = Node(3) 
root.left = Node(4) 
root.right = Node(5) 
root.left.left = Node(6) 
root.left.right = Node(7) 
root.right.left = Node(8) 
root.right.right = Node(9) 
actual = findLCA(root,4,9)
print(actual)


root = Node(3) 
root.left = Node(4) 
root.right = Node(5) 
root.left.left = Node(6) 
root.left.right = Node(7) 
root.right.left = Node(8) 
root.right.right = Node(9) 
actual = findLCA(root,6,7)
print(actual) # 4

  