class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def mirror(root):
    """
    Get left child recursively
    Get right child recusively
    Swap left_Child , right_child with node.left, node.right    
    """
    if root == None:
        return None
    
    left_child = mirror(root.left)
    right_child = mirror(root.right)
    
    root.left, root.right = right_child, left_child
    return root

def printInorder(root): 
    #Practise Yourself :  Write your code Here 
    if root == None:
        return
    
    printInorder(root.left)
    print(root.data)
    printInorder(root.right)


if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)
    
    printInorder(root)
    print("*"*10)
    mirror(root)
    printInorder(root)