import unittest
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return 0
    
    return max(height(root.left), height(root.right)) + 1

def isTreeBalanced(root): 
    """
     a height-balanced binary tree is defined as: a binary tree in which 
     the left and right subtrees of every node differ in height by no more than 1.

     Time complexity: O(n^2), can be optimized to O(n) in the same recursion
                              in place of calling height()

    Real world scenario
    - whether scales of a vegetable weighting machine is balanced or not
    """
    if root == None:
        return True
    
    left = height(root.left)
    right = height(root.right)
    
    # abs(left - right) <= 1 for current node
    # isTreeBalanced(root.left) for left subtree
    # isTreeBalanced(root.right) for right subtree
    if abs(left - right) <= 1 and isTreeBalanced(root.left) and isTreeBalanced(root.right):
        return True
    
    return False

root = Node(2) 
root.left = Node(3) 
root.right = Node(4) 
root.left.left = Node(5) 
root.left.right = Node(6) 
print(isTreeBalanced(root))


root = Node(2) 
root.left = Node(3) 
root.right = Node(4) 
root.left.left = Node(5) 
root.left.left.left = Node(6) 
root.left.left.left.left = Node(9)
print(isTreeBalanced(root))