class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        c=Counter(chain.from_iterable(roads))
        s=set((min(i,j),max(i,j)) for i,j in roads)
        m=0
        for i in range(n):
            for j in range(i+1,n):
                x=c[i]+c[j]
                if (i,j) in s:
                    x-=1
                if x>m:
                    m=x
        return m