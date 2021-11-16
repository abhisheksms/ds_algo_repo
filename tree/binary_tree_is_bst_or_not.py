class Node: 
	def __init__(self, data): 
		self.key = data 
		self.left = None
		self.right = None
	

def isBST(root, min, max):
    """
    WEED OUT EDGE CASES FIRST, THEN RECURSE
    """
    
    if root is None:
        return True
    
    if not min < root.key < max:
        return False
    
    else:
        val1 = isBST(root.left, min, root.key - 1)
        val2 = isBST(root.right, root.key + 1, max)
        return val1 and val2 
    
    
root = Node(12); 
root.left = Node(4); 
root.right = Node(25); 
root.left.left = Node(2); 
root.left.right = Node(9); 
root.right.left = Node(16); 
root.right.right = Node(-32); 
actual = isBST(root, float("-inf"), float("inf"))