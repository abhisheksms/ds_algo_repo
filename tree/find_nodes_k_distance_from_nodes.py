class Node:
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
        
def k_down(root, k, result): 
    """
    Convention k_down(root, k+1) and if val == k get result
    Here k_down(root, k-1) and if k == 0 get result
    """
    if root == None:
        return
    
    if k == 0:
        result.append(root.data)
        return
    
    k_down(root.left, k-1, result)
    k_down(root.right, k-1, result)
    
    return result
  

root = None
root = Node(1)  
root.left = Node(2)  
root.right = Node(3) 
result = []
result = k_down(root,1,result)
print(result)
