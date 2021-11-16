class Node: 
    def __init__(self, key):
	    self.key = key 
	    self.left = self.right = None

def printKDistantfromLeaf(node, k): 
    global MAX_HEIGHT 
    path = [None] * MAX_HEIGHT 
    visited = [False] * MAX_HEIGHT 
    printKDistance(node, k, path, visited, 0) 

def printKDistance(node, k, path, visited, pathlen): 
    if node == None:
        return
    
    path[pathlen] = node.key
    if node.left is None \
       and node.right is None \
       and pathlen - k >= 0 \
       and visited[pathlen - k] == False:
        visited[pathlen - k] = True
        print(path[pathlen - k])
        return
    
    
    printKDistance(node.left, k, path, visited, pathlen+1)
    visited[pathlen-k] = False # backtrack
    printKDistance(node.right, k, path, visited, pathlen+1)

MAX_HEIGHT = 10       


root = Node(3); 
root.left = Node(8); 
root.right = Node(9); 
root.left.left = Node(11); 
root.left.right = Node(7); 
root.left.right.left = Node(6); 
root.left.right.right = Node(12); 
root.right.left = Node(8); 
root.right.right = Node(3); 
actual = printKDistantfromLeaf(root,1)