# Data structure to store a Binary Tree node
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

        
visited_level = 0
def printLeftView(root, level):
    global visited_level
    if root is not None:
        if visited_level < level:
            visited_level = level
            print(root.key)
        
        printLeftView(root.left, level+1)
        printLeftView(root.right, level+1)


if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
    
    # we can also use visited array but
    # need to optimize space
    #visited = [False]*5
    
    # starting from level 1
    printLeftView(root, 1)