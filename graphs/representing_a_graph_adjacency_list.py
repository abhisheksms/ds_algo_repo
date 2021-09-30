#This class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph
        
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)

print(g.graph)