#Represent a node of binary tree  
class Node:  
    def __init__(self,data):  
        self.data = data;  
        self.left = None;  
        self.right = None;  
        
        
class BinaryTreeToDLL:  
    def __init__(self):  
        # #Represent the root of binary tree  
        # self.root = None;  
        
        #Represent the head and tail of the doubly linked list  
        self.head = None;  
        self.tail = None;  
          
    #This function will convert the given binary tree to corresponding doubly linked list  
    def convertbtToDLL(self, node):  
        """
        Video: Global flag
        Code: self.head is None

        1. Recurse to the left most node
        2. set it as self.head (will be None)
        3. now self.tali.right will be node (forward conenction)
        4. node.right will be self.tail (backward connection)
        5. self.tail will be node (move the tail forward)

        Time Complexity O(n) and Space O(Height)
        """
        if node == None:
            return
        
        # left most node is the first node in linked list
        self.convertbtToDLL(node.left)
        if self.head == None:
            self.head = self.tail = node
        else:
            "WE ARE FOCUSSING ONLY ON THE TAIL"
            self.tail.right = node
            node.left = self.tail
            self.tail = node
        
        self.convertbtToDLL(node.right) 

    #display() will print out the nodes of the list  
    def display(self,result):  
        #Node current will point to head  
        current = self.head;  
        if(self.head == None):  
            print("List is empty");  
            return;  
        print("Nodes of generated doubly linked list: ");  
        while(current != None):  
            #Prints each node by incrementing pointer.  
            result.append(current.data),  
            current = current.right;  
            
            
bt = BinaryTreeToDLL();  
#Add nodes to the binary tree  
bt.root = Node(1);  
bt.root.left = Node(2);  
bt.root.right = Node(3);  
bt.root.left.left = Node(4);  
bt.root.left.right = Node(5);  
bt.root.right.left = Node(6);  
bt.root.right.right = Node(7);  
   
#Converts the given binary tree to doubly linked list  
bt.convertbtToDLL(bt.root);  
result = []
#Displays the nodes present in the list  
bt.display(result);
print(result)

