# Data structure to store a Binary Tree node
class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
        
"""
height of a tree

def height(root):
  if root == None:
     return 0

  return max(height(root.left), height(root.right)) + 1
"""

res = 0
def diameter(root):
    """
    # This is basically height of a tree at that node
    1. We will return 1 + max(left_height, right_height) to parent
    2. and diameter calculated as
       diameter = left_height + right_height + 1
    """
    global res
    if root is None:
        return 0
    
    left_height = diameter(root.left)
    right_height = diameter(root.right)
    
    # diameter of given node
    dia = left_height + right_height + 1 
    res = max(res, dia)
    
    # This is basically height of a tree at that node
    return 1 + max(left_height, right_height)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)
actual = diameter(root)
print(res)