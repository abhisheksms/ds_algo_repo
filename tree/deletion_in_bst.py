class Node: 
    def __init__(self, key): 
        self.key = key 
        self.left = None
        self.right = None


def inorder(root): 
    if root is not None: 
        inorder(root.left) 
        print (root.key, end = " ") 
        inorder(root.right) 
        
def insert(node, key): 
    if node is None:
        return Node(key) # return to inner call

    if key < node.key:
        # node is parent
        # node.left is child
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
        
    return node # returns to inner calls/global call


def inorder_successor(node):
    while node.left is not None:
        node = node.left
        
    return node


def Delete(root, key): 
    """
    1. Find until key == root.data
       WE HAVE TO UPDATE THE PARENT POINTER AFTER REACHING THE TARGET NODE
    2. If single node or leaf node, perform standard delete
    3. Else find inorder successor in the right subtree
    
    4. No need to rebalance
       Simply replace the value in this node with the inorder successor
    5. Now delete the original node containing the inorder successor
    """
    if root == None:
        return None
    elif root.key < key:
        #assinging value to keep track of the parents?
        root.right = Delete(root.right, key)
    elif root.key > key:
        root.left = Delete(root.left, key)
    else:
        # single node or leaf node
        # either of these cases will handle the leaf node
        
        # right node empty
        if root.right is None:
            temp = root.left
            root = None
            return temp
        # left node empty
        elif root.left is None:
            temp = root.right
            root = None
            return temp
        
        # find inorder successor
        # min node in right subtree
        # leftmost leaf in right subtree
        temp = inorder_successor(root.right)
        
        # Simply replace the value in this node with the inorder successor
        root.key = temp.key
        
        # Now make the algorithm traverse and
        # delete the original node containing the inorder successor
        # root.right, in argument is the starting point
        root.right = Delete(root.right, temp.key)
    
    return root 


root = None
root = insert(root, 50) 
root = insert(root, 30) 
root = insert(root, 20) 
root = insert(root, 40) 
root = insert(root, 70) 
root = insert(root, 60) 
root = insert(root, 80) 

print ('\nInorder traversal of the given tree')
inorder(root) 

print ('\nDelete 20')
root = Delete(root, 20) 
print ('\nInorder traversal of the modified tree')
inorder(root) 

print ('\nDelete 30')
root = Delete(root, 30) 
print ('\nInorder traversal of the modified tree')
inorder(root) 

print ('\nDelete 50')
root = Delete(root, 50) 
print ('\nInorder traversal of the modified tree')
inorder(root) 