visited=set()
def dfs(grpah,visited,root):
    if root not in visited:
        print (root)
        visited.add(root)
        for next in graph:
            dfs(graph,visited,next)
graph = {
    0: [1, 2, 3], 
    1: [0, 2],   
    2: [0, 1, 4], 
    3: [0],        
    4: [2]         
    }
dfs(graph,visited, 0)