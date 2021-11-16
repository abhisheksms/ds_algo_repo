# A linked list node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
        
def printList(head):
    result = []
    ptr = head
    while ptr:
        result.append(ptr.data)
        ptr = ptr.next
        
    return result


# Iterative function to reverse nodes of linked list
def reverse(head):
    """
    Note: they are REVERSING the links, no swapping is going on
    """
    result = None
    current = head
    # Iterate through the list and move/insert each node to the
    # front of the result list (like a push of the node)
    while current:
        # tricky: note the next node
        next = current.next
        # move the current node onto the result
        current.next = result
        result = current
        # process next node
        current = next
        
    # fix head pointer
    return result
 

def mergeLinkedList(a, b):
    """
    INTITIALIZE A DUMMY POINTER CURR
    point res to curr
    
    start a while loop
    if a is not Node
       curr.next = a
       both curr and a will be curr.next and a.next
    """ 
    # start with a dummy pointer
    curr = Node() # the moving tail
    res = curr # the stationary head
    while a and b:
        """
        For an odd length list, the mid value will automatically be tailed
        along with b
        """
        if a:
            curr.next = a
            curr, a = curr.next, a.next
        
        if b:
            curr.next = b
            curr, b = curr.next, b.next
    
    res = res.next
    return res


# Function to split the linked list into two equal parts and return
# pointer to the second half
def findMiddle(head):
    #Practise Yourself :  Write your code Here 
    slow = fast = head
    
    # find middle pointer
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow 



def rearrange(head):
    # base case
    if head is None:
        return
    # find second half of linked list
    mid = findMiddle(head) 
    
    # break the chain
    ptr = head
    while ptr.next != mid:
        ptr = ptr.next 
    ptr.next = None
    
    # reverse the second half
    mid = reverse(mid)
    
    
    
    # merge first and second half
    res = mergeLinkedList(head, mid)
    return res
    
        
head = None

# 5 4 3 2 1 0
for i in reversed(range(6)):
    head = Node(i + 1, head)
    


print("Before")
print(printList(head))

res = rearrange(head)
print("After")
print(printList(res))