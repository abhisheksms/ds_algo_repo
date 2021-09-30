from collections import defaultdict
class AllPaths:
    def __init__(self):
        self.graph = defaultdict(list)
        # also we can use a visited array, but defaultdict is a better option
        self.visited = defaultdict(int)
        self.res = []
        
    def add_edge(self, src, dest):
        self.graph[src].append(dest)
        
    def dfs(self, src, dest):
        # to ensure source is not visited again by its children
        if not self.res:
            self.visited[src] = 1
            self.res.append(src)
            
        if src == dest:
            print(self.res)
            return
        
        for i in self.graph[src]:
            if not self.visited[i]:
                self.res.append(i)
                self.visited[i] = 1
                
                self.dfs(i, dest)
                
                self.res.pop()
                self.visited[i] = 0
                
            

g = AllPaths()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 0)
g.add_edge(1, 3)
g.add_edge(3, 2)

g.dfs(1, 2)
