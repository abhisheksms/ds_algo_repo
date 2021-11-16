class Node:
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
    
def sum_tree(root):
    if root == None:
        return 0
    
    left_child = sum_tree(root.left)
    right_child = sum_tree(root.right)
    
    old_val = root.data
    root.data = left_child + right_child
    return left_child + right_child + old_val 

def inorder(root):
    if root == None:
        return
    
    inorder(root.left)
    print(root.data)
    inorder(root.right)
    

root = None
root = Node(10)  
root.left = Node(-2)  
root.right = Node(6)  
root.left.left = Node(8)  
root.left.right = Node(-4)  
root.right.left = Node(7)  
root.right.right = Node(5)  
resultRoot = sum_tree(root)
print(resultRoot)

inorder(root)
#print ('Max path sum is' , result)



