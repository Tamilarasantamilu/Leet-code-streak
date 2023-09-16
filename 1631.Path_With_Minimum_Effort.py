class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dst = (len(heights)-1, len(heights[0])-1)
        dist = [[float("inf")]*len(heights[0]) for _ in range(len(heights))]
        dist[0][0] = 0;
        min_heap = [(0, 0, 0)]
        lookup = [[False]*len(heights[0]) for _ in range(len(heights))]
        while min_heap:
            d, r, c = heapq.heappop(min_heap)
            if lookup[r][c]:
                continue
            lookup[r][c] = True
            if (r, c) == dst:
                return d
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if not (0 <= nr < len(heights) and 0 <= nc < len(heights[0]) and not lookup[nr][nc]):
                    continue
                nd = max(d, abs(heights[nr][nc]-heights[r][c]))
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    heapq.heappush(min_heap, (nd, nr, nc))
        return -1
