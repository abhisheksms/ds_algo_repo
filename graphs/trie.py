
class TrieNode:
    def __init__(self, char):
        #self.char = char # not needed
        self.is_end = False # used while printing the trie in dfs fashion
        self.children = {}
        
class Trie:
    """
    We have named the root as Trie
    """
    def __init__(self):
        self.root = TrieNode("")
        
    def insert(self, word):        
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode(char))
            # if char in node.children:
            #     node = node.children[char]
            # else:
            #     node.children[char] = TrieNode(char)
            #     node = node.children[char]
            #     # new_node = TrieNode(char)
            #     # node.children[char] = new_node
            #     # node = new_node
                
        node.is_end = True
        
    def dfs(self, ptr):
        """
        printing values
        """
        if ptr.is_end:
            return
        
        for char in ptr.children:
            print(char)
            self.dfs(ptr.children[char])
        
        
    def search(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                print("Not found")
                return
                
        print("Found")
    
    
                
t = Trie()
t.insert("was")
t.insert("word")
t.insert("war")
t.insert("what")
t.insert("where")

t.search("warn")
t.search("war")
# print(t.root)
# t.dfs(t.root)