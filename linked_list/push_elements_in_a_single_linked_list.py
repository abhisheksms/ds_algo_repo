class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        

def printList(head):
    ptr = head
    result = []
    while ptr:
        result.append(ptr.data)
        ptr = ptr.next
        
    return result

head = None
tail = None
for i in range(5):
    node = Node(i+1)
    if head is None:
        head = tail = node
    else:
        tail.next = node
        tail = node


print(printList(head))