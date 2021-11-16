# A linked list node
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
# Function to print given linked list
def printList(head):
    result = []
    ptr = head
    while ptr:
        result.append(ptr.data)
        ptr = ptr.next
        
    return result


# recursively
def reverse(head):
    if head is None or head.next is None:
        return head
    
    # recurse forwards
    rev_head = reverse(head.next)
    print(rev_head.data)
    
    # reverse the previous pointer
    head.next.next = head
    
    #current pointer temporarily points to None
    head.next = None
    
    return rev_head
    
    
head = None  
tail = None

# one way to push nodes
# for i in range(5):
#     node = Node(i+1)
#     if head == None:
#         head = node
#         tail = head
#     else:
#         ptr = head
#         while ptr.next is not None:
#             ptr = ptr.next
#         ptr.next = node

# another way to push nodes
#4 3 2 1 0
for i in reversed(range(5)):
    node = Node(i+1)
    node.next = head
    head = node
    

# rearrange(head)
print("Before")
print(printList(head))

new_head = reverse(head)
print("After")
print(printList(new_head))