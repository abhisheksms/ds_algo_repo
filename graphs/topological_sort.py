#This class represents a directed graph using adjacency list representation
from collections import defaultdict
class Graph:
    """
    Time complexity: O(V+E)
    Space complexity: O(V)
    """
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = defaultdict(list)
        self.top_sort = []
        self.visited = [0]*num_vertices
        
    def add(self,src,dest):
        self.graph[src].append(dest)
        
    def dfs(self, val):
        self.visited[val] = 1
        for i in self.graph[val]:
            if not self.visited[i]:
                self.dfs(i)

        # if all neighbours visited   
        self.top_sort.insert(0, val)
        
    def topological_sort(self):
        # find element with min indegree
        # for loop to ensure we cover cliques as well
        for i in range(self.num_vertices):
            if not self.visited[i]:
                self.dfs(i)
        
        return self.top_sort
                

g = Graph(6)
g.add(5,0)
g.add(4,0)
g.add(5,2)
g.add(4,1)
g.add(2,3)
g.add(3,1)

print(g.graph)
print(g.topological_sort())

