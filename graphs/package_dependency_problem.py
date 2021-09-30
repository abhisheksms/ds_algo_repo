from collections import defaultdict
class FindPrerequisites:
    """
    Time complexity: O(n)
    """
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
        self.modified_top_sort = []
        self.visited = [0]*vertices
        
    def add(self, src, dest):
        self.graph[src].append(dest)
        
    def dfs(self, i):
        self.visited[i] = 1
        for j in self.graph[i]:
            if not self.visited[j]:
                self.dfs(j)
                
        self.modified_top_sort.append(i) #typically it self.top_sort.insert(0, val)
        
    def top_sort(self):
        for i in range(self.vertices):
            if not self.visited[i]:
                self.dfs(i)
                
        return self.modified_top_sort
             
g = FindPrerequisites(4)
nodes = [[1,0],[2,0],[3,1],[3,2]]

for n in nodes:
    g.add(n[0], n[1])
    
print(g.top_sort())