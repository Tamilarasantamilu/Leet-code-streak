class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n=len(profits)
        c_p = list(zip(capital, profits))
        c_p.sort()

        pq=[]
        curr=0
        for i in range(k):
            while curr<n and c_p[curr][0]<=w:
                heapq.heappush(pq, -c_p[curr][1])
                curr+=1
            if pq: w-=heapq.heappop(pq)
            else: break
        return w
