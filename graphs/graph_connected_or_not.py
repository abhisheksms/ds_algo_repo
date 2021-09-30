def is_strongly_connected():  
    """
    Time complexity: O(V+E) for a graph represented using adjacency list.
                     Note: here we are using adjacency matrix
    Space complexity: O(n^2)
    """ 
    for i in range(4): #we are creting a zero visited array for every element
        visited = [0]*4 
        dfs(i, visited) 
            
        for j in range(4):
            if not visited[j]:
                return False
        
    return True


def dfs(i, visited):
    print(i, visited)
    visited[i] = 1
    for z in range(4):
        if grid[i][z] and not visited[z]:
            dfs(z, visited)

global grid
grid = [[0, 1, 0, 0],
        [1, 0, 0, 1],
        [0, 0, 0, 0],
        [1, 0, 1, 0]]
print(is_strongly_connected())
