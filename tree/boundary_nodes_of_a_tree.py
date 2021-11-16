class Node: 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
#function to print leaf nodes of a Binary Tree  

def left_only(node):
    if node is not None:
        if node.left is not None:
            print(node.data)
            left_only(node.left)
        elif node.right is not None:
            print(node.data)
            # we are going right, as left was None
            left_only(node.right)

def right_only(node):
    if node is not None:
        if node.right is not None:
            right_only(node.right)
            print(node.data)
        elif node.left is not None:
            right_only(node.left)
            print(node.data)

def leaf_nodes(node):
    if node is not None:
        leaf_nodes(node.left)
        if node.left is None and node.right is None:
            print(node.data)
        leaf_nodes(node.right)
    

# Function to do boundary traversal of a given binary tree 
def printBoundary(root):
    """ 
    Where we differed:
   - Have modular methods, which only return the given nodes
   - We thought of going left only for nodes
     We should have gone right as well(if left is None) 
     and then continue left again
   - For a leaf node, node.left and node.right is None
   - For right internal nodes
     
     # if moving in anti clockwise direction(from child to parent)
     # recursion then print/append
     if node is not None:
         if node.right is not None:
             func_call(node.right)
             print(node.key)

     # if moving from parent to child
     # print/append then recursion
     if node is not None:
         if node.left is not None:
             print(node.key)
             func_call(node.left)
             
    ********************************************        
    Time complexity: O(n)
    """
    print(root.data)
    left_only(root.left)
    leaf_nodes(root)
    right_only(root.right)

root = None
root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)
# printBoundary(root) 

# 20 8 4 10 14 25 22

result = []
result = printBoundary(root)