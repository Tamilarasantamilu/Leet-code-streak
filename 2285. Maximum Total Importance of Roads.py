class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0] * n
        
        for u, v in roads:
            degrees[u] += 1
            degrees[v] += 1
        
        nodes_with_degrees = [(i, degrees[i]) for i in range(n)]
        nodes_with_degrees.sort(key=lambda x: -x[1])
        
        importance = [0] * n
        for i, (node, degree) in enumerate(nodes_with_degrees):
            importance[node] = n - i
        
        total_importance = 0
        for u, v in roads:
            total_importance += importance[u] + importance[v]
        
        return total_importance
