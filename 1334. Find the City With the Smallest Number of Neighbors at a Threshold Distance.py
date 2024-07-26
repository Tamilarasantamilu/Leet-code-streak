class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Initialize the distance matrix with infinity
        dist = [[float('inf')] * n for _ in range(n)]
        
        # Distance to itself is 0
        for i in range(n):
            dist[i][i] = 0
        
        # Update the distance matrix with the given edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Floyd-Warshall algorithm to find shortest paths between all pairs of cities
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Find the city with the smallest number of neighbors within the distance threshold
        min_count = float('inf')
        result_city = -1
        
        for i in range(n):
            count = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    count += 1
            if count <= min_count:
                min_count = count
                result_city = i
        
        return result_city
