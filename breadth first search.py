import collections
def bfs(graph, root):
    visited = set()  # A set to keep track of the visited nodes
    queue = collections.deque([root])  # Queue to manage the BFS process. We start with the root node.
    while queue:                        # while there are nodes in the queue
        vertex = queue.popleft()        #pop the first element from the queue
        if vertex not in visited:              # If the node has not been visited, visit it and mark it as visited
            visited.add(vertex)
            print(vertex)  # Print the current node
            # Add all unvisited neighbors of the current node to the queue
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

if __name__ == '__main__':
    graph = {
        0: [1, 2, 3], 
        1: [0, 2],
        2: [0, 1, 4],  
        3: [0],       
        4: [2]         
    }
    bfs(graph, 0)
