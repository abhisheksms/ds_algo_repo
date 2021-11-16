class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end = True
        
    def search(self, word):
        """
        We are trying to shorten the approach
        Brain is trying to conserve memory for something which I don't know
        """
        node = self.root
        for char in word:
            if not node.is_end and char in node.children:
                node = node.children[char]
            else:
                return "Not found"
            
        return "Found"
    
    def dfs(self, node, res):
        if node.is_end:
            print(res)
            return
            
        for char in node.children:
            self.dfs(node.children[char], res + char)
        
    
    def autocomplete(self, sub_word):
        # reach the end char in trie
        node = self.root
        for char in sub_word:
            if not node.is_end and char in node.children:
                node = node.children[char]
        self.dfs(node, sub_word)


t = Trie()
t.insert("district")
t.insert("dimension")
t.insert("discourage")

print(t.search("dimension"))
t.autocomplete("dis")

# print(t.autocomplete("dim"))
