from collections import defaultdict
class AlienDictionary:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visit_count = defaultdict(int)
        self.visited = defaultdict(int)
        self.res = []
        
    def add_edge(self, src, dest):
        self.visited[src] = 0
        self.visited[dest] = 0
    
        if src not in self.visit_count:
            self.visit_count[src] = 0
        self.visit_count[dest] += 1 
        
        if dest not in self.graph:
            self.graph[dest] = []        
        self.graph[src].append(dest)

        
    def create_graph(self, dictionary):
        n = len(dictionary)
        for i in range(n-1):
            sa = dictionary[i]
            sb = dictionary[i+1]
            
            i = 0
            while i < len(sa) and i < len(sb):
                if sa[i] != sb[i]:
                    self.add_edge(sa[i], sb[i])
                    break
                i += 1
                
    # recursive approach
    def top_sort_recursive(self):
        for v in self.visit_count:
            
            if self.visit_count[v] == 0:
                self.res.append(v)
                for g in self.graph[v]:
                    self.visit_count[g] = max(0, self.visit_count[g]-1)
                    
                # ensure this node is not seen again
                # we used a separate visited array to mark it as visited
                del self.visit_count[v]
                self.top_sort_recursive()
                break
                                
                
    # iterative approach
    def top_sort(self):
        for _ in range(len(self.visited)):
            for k, v in self.visit_count.items():
                if v <= 0 and not self.visited[k]:
                    self.visited[k] = 1
                    self.res.append(k)
                    for k1 in self.graph[k]:
                        self.visit_count[k1] -= 1
                    
        return self.res
        
            

# dictionary = ['cca','aaa','aab']
dictionary = ["baa", "abcd", "abca", "cab", "cad"]
# dictionary = ['yxx','xyzt','xyzx', 'zxy', 'zxt']
g = AlienDictionary()
g.create_graph(dictionary)
# print(g.graph)
# print(g.visit_count)

# print(g.top_sort())
print(g.top_sort_recursive())
print(g.res)
# 

#     compare(sa,sb)