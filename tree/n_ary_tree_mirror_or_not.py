class Node : 
    def __init__(self ,key): 
        self.key = key  
        self.child = [] 
        
d = [] # stack
e = [] # queue
def stack_tree(root1):
    """
    Fifo property of queue
    Lifo property of stack

    first tree :Parent first - stack
    second tree :Child first - queue

    Think from perspective of parent
    In stack: parent is required pushed first(hence popped last)
    So in queue it should be pushed last

    Time and Space Complexity O(n)
    """
    global d
    if root1 == None:
        return
    
    d.append(root1.key) # add the parent first
    for child_node in root1.child:
        stack_tree(child_node)
        

def queue_tree(root2):
    global e
    if root2 == None:
        return
        
    for child_node in root2.child:
        queue_tree(child_node)
    e.append(root2.key)  # add the children first
          
root = Node(10) 
root.child.append(Node(2)) 
root.child.append(Node(34)) 
root.child.append(Node(56)) 
root.child.append(Node(100)) 
root.child[2].child.append(Node(1)) 
root.child[3].child.append(Node(7)) 
root.child[3].child.append(Node(8)) 
root.child[3].child.append(Node(9)) 
  

stack_tree(root)
print(d)
# printNodeLevelWise(root) 
  
root2 = Node(10) 
root2.child.append(Node(100)) 
root2.child.append(Node(56)) 
root2.child.append(Node(34)) 
root2.child.append(Node(2)) 
root2.child[0].child.append(Node(9)) 
root2.child[0].child.append(Node(8)) 
root2.child[0].child.append(Node(7)) 
root2.child[1].child.append(Node(1)) 

queue_tree(root2)
print(e) 
      
# printNodeLevelWise(root) 

