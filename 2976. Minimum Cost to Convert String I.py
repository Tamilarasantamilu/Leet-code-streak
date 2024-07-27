class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)
        INF = float('inf')
        
        # Number of different lowercase English letters
        NUM_LETTERS = 26
        
        # Create a cost matrix initialized to INF
        dist = [[INF] * NUM_LETTERS for _ in range(NUM_LETTERS)]
        
        # Initialize the diagonal to 0 (cost to transform a character to itself)
        for i in range(NUM_LETTERS):
            dist[i][i] = 0
        
        # Populate the cost matrix with the given transformation costs
        for o, c, z in zip(original, changed, cost):
            dist[ord(o) - ord('a')][ord(c) - ord('a')] = min(dist[ord(o) - ord('a')][ord(c) - ord('a')], z)
        
        # Floyd-Warshall algorithm to find the shortest paths between all pairs of nodes
        for k in range(NUM_LETTERS):
            for i in range(NUM_LETTERS):
                for j in range(NUM_LETTERS):
                    if dist[i][k] < INF and dist[k][j] < INF:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        # Calculate the minimum cost to transform source to target
        total_cost = 0
        for s_char, t_char in zip(source, target):
            s_idx = ord(s_char) - ord('a')
            t_idx = ord(t_char) - ord('a')
            if dist[s_idx][t_idx] == INF:
                return -1
            total_cost += dist[s_idx][t_idx]
        
        return total_cost
