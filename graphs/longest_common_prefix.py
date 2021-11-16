class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
        

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, arr):
        for word in arr:
            node = self.root
            for char in word:
                # dict.setdefault(key, value)
                node = node.children.setdefault(char, TrieNode())
#                 if char not in node.children:
#                     node.children[char] = TrieNode()                   
#                 node = node.children[char]

            node.is_end = True
    
    def determine_longest_prefix(self):
        ptr = self.root
        res = ""
        
        while not ptr.is_end and len(ptr.children.keys()) == 1:
            for k, v in ptr.children.items():
                res += k
                ptr = ptr.children[k]
        
        return res
        
    
arr = ["flower","flow","flight"] 
t = Trie()
t.insert(arr)
print(t.determine_longest_prefix())