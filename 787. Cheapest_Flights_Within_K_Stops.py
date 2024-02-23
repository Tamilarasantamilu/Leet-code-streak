class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        cost = [float('inf')] * n
        cost[src] = 0

        # Bellman-Ford Algorithm
        for _ in range(k+1):
            temp = list(cost) 
            for flight in flights:
                u, v, w = flight
                temp[v] = min(temp[v], cost[u] + w)
            cost = temp

        return cost[dst] if cost[dst] != float('inf') else -1
