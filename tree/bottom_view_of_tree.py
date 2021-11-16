# Data structure to store a Binary Tree node
class Node:
	def __init__(self, key=None, left=None, right=None):
		self.key = key
		self.left = left
		self.right = right
        
hmap = {}
def bottom(root, dist):
    if root is None:
        return
    
    hmap[dist] = root.key
    bottom(root.left, dist-1)
    bottom(root.right, dist+1)
        

# Function to print the bottom view of given binary tree
def bottamViewView(root):
    bottom(root, 0)
    return [v for k, v in hmap.items()]
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)
result = []
result = bottamViewView(root)
print(result)
        
