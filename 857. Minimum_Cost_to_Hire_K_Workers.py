import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        workers = sorted((wage[i] / quality[i], quality[i]) for i in range(n))
        ans = float('inf')
        sumq = 0
        heap = []

        for ratio, qual in workers:
            heapq.heappush(heap, -qual)
            sumq += qual

            if len(heap) > k:
                sumq += heapq.heappop(heap)

            if len(heap) == k:
                ans = min(ans, sumq * ratio)

        return ans
