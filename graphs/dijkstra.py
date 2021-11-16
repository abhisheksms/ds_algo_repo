def get_min_unvisited_vertex(value, n, visited):
    min_val = float("inf")
    min_vertex = -99999
    
    for i in range(n):
        if min_val > value[i] and not visited[i]:
            min_val = value[i]
            min_vertex = i
            
    return min_vertex

def dijkstra(graph):
    """
    - initialize parent (all -1)
                 value(all inf except zero for source) and 
                 visited array(all 0)
    - for visited use a hash map for non sequential elements
    - get vertex with minimum value
    - if its neighbours have greater value than current vertex + edge weight
      and it's not visited then
    - then relax the neighbour
      update parent to current node, value with new value,
    - mark the current minumum vertesx as visited
    - the process of finding next minimum vertex runs n-1 times
      as for last node all neighbours will be visited


    T.C O(V^2) OR O(VlogV) with priority queue
    S.C O(VlogV)
    """
    n =len(graph)
    # initialize = 
    parent = [-1]*n
    value = [float("inf")]*n
    value[0] = 0
    visited = [0]*n
    
    for _ in range(n-1):
        min_vertex = get_min_unvisited_vertex(value, n, visited)
        visited[min_vertex] = 1
        neighbours = graph[min_vertex]
        
        for i in range(n):
            val = graph[min_vertex][i]
            if val and not visited[i] and value[min_vertex] + val < value[i]:
                value[i] = value[min_vertex] + val
                parent[i] = min_vertex

    print(visited)
    return parent


graph = [
     [0, 1, 4, 0, 0, 0],
     [1, 0, 4, 2, 7, 0],
    [4, 4, 0, 3, 5, 0],
    [0, 2, 3, 0, 4, 6],
    [0, 7, 5, 4, 0, 7],
    [0, 0, 0, 6, 7, 0]
]

print(dijkstra(graph))
