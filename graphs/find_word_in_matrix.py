from itertools import product

class TrieNode:
    def __init__(self, char):
        self.children = {}
        self.is_end = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode("")
        
    def insert(self, word):
        # trie which will be descended through the hierarchy
        node = self.root
        
        for char in word:
            # if char present then node = node.children[char]
            # else node.children[char] = TrieNode(char) and node = node,children[char]
            node = node.children.setdefault(char, TrieNode(char))
                
        node.is_end = True
        
    def create_trie(self, words):
        for word in words:
            self.insert(word)
            
    def search(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                print("Not Found")
                return
            
        print("Found")
        
row_list = [-1, -1, -1, 0, 1, 0, 1, 1]
col_list = [-1, 1, 0, -1, -1, 1, 0, 1]

def is_valid(x, y, visited, board, ch):
    return (0 <= x < M) and (0 <= y < N) and \
           not visited[x][y] and (board[x][y] == ch)
    
    
# searchBoggle(root.character[ch], board, i, j, processed, ch, result)
def search_trie_and_matrix(root, i, j, board, visited, path, result):
    if root.is_end:
        result.add(path)
        
    visited[i][j] = True

    for key, value in root.children.items():
        for x, y in zip(row_list, col_list):
            new_x = i + x
            new_y = j + y
            
            # here key is the character
            if is_valid(new_x, new_y, visited, board, key):
                # value is root.children[key]
                search_trie_and_matrix(value, new_x, new_y, board, visited, path + key, result)
        
        
         
    visited[i][j] = False
        
        
        
def search_word(words, board):
    # i.e self.root
    t = Trie()
    t.create_trie(words)
    result = set()  
    root = t.root
    
    # print(root.children)
    
    row, col = len(board), len(board[0])
    # for every word
    visited = [[False]*col for _ in range(row)]
    
    for i, j in itertools.product(range(row), range(col)):
        ch = board[i][j]
        # proceed only if current character is child of the Trie root node
        if ch in root.children:
            search_trie_and_matrix(root.children[ch], i, j, board, visited, ch, result)

    # result.add() kya??
    print(result)
    
        
        
            


board = [
        ['M', 'S', 'E', 'F'],
        ['R', 'A', 'T', 'D'],
        ['L', 'O', 'N', 'E'],
        ['K', 'A', 'F', 'B']
    ]

(M, N) = (len(board), len(board[0]))
words = ["START", "NOTE", "SAND", "STONED"]
search_word(words, board)