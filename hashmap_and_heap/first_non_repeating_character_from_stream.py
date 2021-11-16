class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
def find_nonrepeating_character(s):
    # serves as our hashmap
    head = tail = None
    ascii_array = [None]*26
    head = tail = None
    
    for ch in s:
        val = ord(ch)%97
        
        if ascii_array[val] != " ":
            if ascii_array[val] != None:
                del_node = ascii_array[val]
                if head == del_node:
                    head = del_node.next
                elif del_node.next == tail:
                    tail = del_node.prev
                else:
                    prev_node = del_node.prev
                    next_node = del_node.next

                    prev_node.next = next_node
                    next_node.prev = prev_node
                
                ascii_array[val] = " "
            else:
                node = Node(ch)
                ascii_array[val] = node
                if head == None:
                    head = tail = node
                else:
                    node.prev = tail
                    tail.next = node
                    tail = node
        
        if head:
            print(head.data)
        else:
            print(-1)

# s = "acdcfa"
s = "aabcdcfb"
find_nonrepeating_character(s)