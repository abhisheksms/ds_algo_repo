class Node:
     # A constructor to create a new node  
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
        
def k_down(node, k):
    if node == None or k < 0:
        return
    
    if k == 0:
        print(node.data)
        return
    
    k_down(node.left, k-1)
    k_down(node.right, k-1)

# Prints all nodes at distance k from a given target node 
# The k distant nodes may be upward or downward. This function 
# returns distance of root from target node, it returns -1  
# if target node is not present in tree rooted with root
def printNodes(node, target, k):
    """
    1. k is decremented (in fucntion call) when we move upwards
    2. If TARGET found on the right, serach for K-DISTANCE nodes on the left

    Another approach: Convert tree to graph in adjaceny list representation and perform bfs
    """
    if node == None:
        return -1
    
    if node == target:
        k_down(node, k)
        return 1
    
    dleft = printNodes(node.left, target, k)
    if dleft != -1:
        if dleft == k:
            print(node.data)
        else:
            k_down(node.right, k - dleft - 1)
            
        return 1 + dleft
    
    
    dright = printNodes(node.right, target, k)
    if dright != -1:
        if dright == k:
            print(node.data)
        else:
            k_down(node.left, k-dright-1)
        
        return 1 + dright
    
    # if both dleft and dright is -1
    return -1
    
root = Node(20) 
root.left = Node(8) 
root.right = Node(22) 
root.left.left = Node(4) 
root.left.right = Node(12) 
root.left.right.left = Node(10) 
root.left.right.right = Node(14) 
target = root.left.right 
printNodes(root, target, 2) 