import heapq
from collections import defaultdict
from typing import List, Dict, Tuple

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        """
        Calculates the maximum probability of reaching the end_node from the start_node
        using the given edges and their success probabilities.
        
        Args:
        - n: Total number of nodes.
        - edges: List of edges where each edge connects two nodes [u, v].
        - succProb: List of success probabilities corresponding to each edge.
        - start_node: The node to start the search from.
        - end_node: The target node to reach.

        Returns:
        - The maximum probability to reach the end_node. Returns 0 if the end_node is not reachable.

        Time Complexity: O((E + N) log N), where E is the number of edges and N is the number of nodes.
        Space Complexity: O(E + N), for storing the adjacency list, priority queue, and visited set.
        """
        
        # Build the graph using edges and their corresponding success probabilities
        adjacency_list = self.build_graph(edges, succProb)
        
        # Priority queue (max-heap) initialized with the start node and a probability of 1
        # The probability is negated to use Python's min-heap as a max-heap
        max_heap = [(-1.0, start_node)]
        
        # Set to keep track of visited nodes to avoid revisiting them
        visited_nodes = set()

        # Process the nodes in the priority queue
        while max_heap:
            # Pop the node with the highest probability
            current_probability, current_node = heapq.heappop(max_heap)
            
            # If the end_node is reached, return the positive probability
            if current_node == end_node:
                return -current_probability
            
            # Mark the current node as visited
            visited_nodes.add(current_node)
            
            # Explore the neighbors of the current node
            for neighbor, edge_probability in adjacency_list.get(current_node, []):
                if neighbor not in visited_nodes:
                    # Push the new probability and the neighbor to the priority queue
                    heapq.heappush(max_heap, (current_probability * edge_probability, neighbor))
        
        # If the end_node is unreachable, return 0
        return 0
    
    def build_graph(self, edges: List[List[int]], probability_list: List[float]) -> Dict[int, List[Tuple[int, float]]]:
        """
        Builds a graph as an adjacency list where each node is connected to its neighbors
        along with the corresponding success probability of the edge.
        
        Args:
        - edges: List of edges where each edge connects two nodes [u, v].
        - probability_list: List of success probabilities corresponding to each edge.

        Returns:
        - A dictionary representing the adjacency list of the graph.
        """
        adjacency_list = defaultdict(list)
        for i, (source_node, destination_node) in enumerate(edges):
            # Add the edge to the graph with its corresponding success probability
            adjacency_list[source_node].append((destination_node, probability_list[i]))
            adjacency_list[destination_node].append((source_node, probability_list[i]))
        return adjacency_list
