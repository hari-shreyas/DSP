import collections
def dfs(graph, root):
    visited = set()  # A set to keep track of the visited nodes
    stack = collections.deque([root])  # Stack to manage the DFS process. We start with the root node.
    # While there are nodes in the stack to process
    while stack:
        # Pop the last node from the stack for processing (LIFO)
        vertex = stack.pop()
        # If the node has not been visited yet, process it
        if vertex not in visited:
            print(vertex)  # Print the current node (for demonstration purposes)
            visited.add(vertex)  # Mark the node as visited
            # Add all unvisited neighbors of the current node to the stack
            # We reverse the neighbors to maintain the correct DFS order (left-to-right)
            stack.extend(reversed(graph[vertex]))

if __name__ == '__main__':
    graph = {
        0: [1, 2, 3], 
        1: [0, 2],   
        2: [0, 1, 4], 
        3: [0],        
        4: [2]         
    }
    dfs(graph, 0)
