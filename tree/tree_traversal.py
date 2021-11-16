class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
        
# ANOTHER APPROACH

# def inorder(root): 
# 	if root is not None: 
# 		inorder(root.left) 
# 		print (root.key) 
# 		inorder(root.right) 


def printInorder(root): 
    #Practise Yourself :  Write your code Here 
    if root == None:
        return
    
    printInorder(root.left)
    print(root.val)
    printInorder(root.right)

    
def printPostorder(root): 
    #Practise Yourself :  Write your code Here 
    if root == None:
        return
    
    printInorder(root.left)
    printInorder(root.right)
    print(root.val)

    
def printPreorder(root): 
    #Practise Yourself :  Write your code Here 
    if root == None:
        return
    
    print(root.val)
    printInorder(root.left)
    printInorder(root.right)
    
        

root = Node(1) 
root.left  = Node(2) 
root.right  = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5) 

printPreorder(root) 
print("*"*10) 
printInorder(root) 
print("*"*10) 
printPostorder(root) 