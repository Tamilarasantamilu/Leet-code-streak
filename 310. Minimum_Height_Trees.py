class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
      
        # Initialize a graph and a degree list to store the degree of each node
        graph = defaultdict(list)
        degree = [0] * n
      
        # Build the graph and keep track of each node's degree
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            degree[node1] += 1
            degree[node2] += 1
      
        # Initialize a queue with all leaf nodes (nodes with degree 1)
        leaves_queue = deque(i for i in range(n) if degree[i] == 1)
        min_height_trees = []
      
        # Keep trimming leaves until the centroid/s is/are found
        while leaves_queue:
            min_height_trees.clear()
            # Process all current leaves
            for _ in range(len(leaves_queue)):
                current_node = leaves_queue.popleft()
                min_height_trees.append(current_node)
                # Update the degrees of the current node's neighbors
                for neighbor in graph[current_node]:
                    degree[neighbor] -= 1
                    # If the neighbor has become a leaf, add it to the queue for processing in the next round
                    if degree[neighbor] == 1:
                        leaves_queue.append(neighbor)
      
        # Return the final centroids of the tree, which will have minimum height
        return min_height_trees
