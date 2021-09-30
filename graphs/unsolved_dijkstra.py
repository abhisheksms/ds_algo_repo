from collections import defaultdict
import heapq

class Node:
    def __init__(self, prev_node, distance):
        self.prev_node = prev_node
        self.distance = distance
        
# class PriorityQueue:
#     def __init__(self, current, distance):
#         self.current = current
#         self.distance = distance
        

class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
    
               
class Dijkstra:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
        self.visited = [0]*vertices
        self.hash_map = {i : [-1, float("inf")] if i != 0 else [0,0] for i in range(6)}
        self.priority_queue = []
        
    def add_edge(self, edge):
        self.graph[edge.src].append([edge.dest, edge.weight])
        
        
# hash_map = {node_id: [prev,distance]}
#

#create graph
g = Dijkstra(6)
g.add_edge(Edge(0,1,10))
g.add_edge(Edge(0,2,15))
g.add_edge(Edge(1,4,15))
g.add_edge(Edge(1,3,12))
g.add_edge(Edge(2,5,10))
g.add_edge(Edge(3,4,1))
g.add_edge(Edge(3,5,2))
g.add_edge(Edge(4,5,5))

print(g.graph)
print(g.hash_map)