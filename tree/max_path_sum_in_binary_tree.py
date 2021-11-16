class Node:
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
    

result = 0
def findMaxPathSumBT(root):
    """
    - You need max of something, what is it??
     
    - max_value = max(node.data, node.data + max(left_child, right_child))
        max_top = max(max_value, node.data + left_child + right_child)
        result = max(result, max_top)
        return max_value

        # This problem is similar to kadane
        # max_value resembles max_c
        # result/max_top resembles max_g
    - WE ALWAYS KEEP THE MAX OF THE LEFT OR RIGHT HALF FROM THE LOWER SUBTREES
        IN max_value(max_c)
    """
    #Practise Yourself :  Write your code Here 
    global result
    if root == None:
        return 0
    
    left_child = findMaxPathSumBT(root.left)
    right_child = findMaxPathSumBT(root.right)
    
    max_value = max(root.data, root.data + max(left_child, right_child))
    max_top = max(max_value, root.data+left_child+right_child)
    result = max(result, max_top)
    return max_value 
    

root = Node(10) 
root.left = Node(2)
root.right = Node(15)
root.left.left = Node(-4)
root.left.right = Node(-6) 
root.left.left.left = Node(28)
root.left.left.right = Node(-22)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
findMaxPathSumBT(root)
print(result)
#print ('Max path sum is' , result)



