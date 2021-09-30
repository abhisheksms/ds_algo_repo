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
        
    def add(self,src,dest):
        self.graph[src].append(dest)
        
    def check_cycle(self, index, visited, parent):
        visited[index] = 1
        
        for val in self.graph[index]:
            if not visited[val]:
                if self.check_cycle(val, visited, parent):
                    return True
            elif val != parent:
                return True
    
        return False
    

g = Graph(6)
g.add(0,1)
g.add(0,2)
g.add(1,4)
g.add(1,3)
g.add(4,5)
g.add(3,5)

visited = [0]*6
print(g.graph)
print(g.check_cycle(0, visited, -1))