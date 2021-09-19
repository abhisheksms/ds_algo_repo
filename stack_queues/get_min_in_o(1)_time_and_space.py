class Stack:
    """
    while pushing:
        new_val = 2*current_element(seen in array) - previous_minimum_value

        if x < minele
            store(2x - minele)
            minele = x

        as 2x - minele  always less than

    while popping
        previous_minimum_value = 2*current_minimum_value - current_element(seen in stack)

        if y < minele
            minele = 2*minele - y

    We are not converned about peek operation
    """
    def __init__(self):
        self.s = []
        self.min_elem = 0
    
    def getmin(self):
        print(self.min_elem)
    
    def push(self, elem):
        if len(self.s) == 0:
            self.s.append(elem)
            self.min_elem = elem
        elif elem < self.min_elem:
            self.s.append(2*elem - self.min_elem)
            self.min_elem = elem 
        else:
            self.s.append(elem)
            
            
    def showall(self):
        print(self.s)
        
    def pop(self):
        if len(self.s) == 1:
            self.s.append(elem)
            self.min_elem = elem
        else:
            top_val = self.s.pop()
            if top_val < self.min_elem:
                self.min_elem = 2*self.min_elem - top_val
            
st = Stack()
st.push(3)
st.push(5)
st.push(2)
st.push(1)
st.push(1)
st.push(-1)
st.getmin()
st.pop()
st.getmin()
st.pop()
st.pop()
st.pop()
st.getmin()
st.showall()