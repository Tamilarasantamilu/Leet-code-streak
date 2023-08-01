from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        l=[i for i in range(1,n+1)]
        c=combinations(l,k)
        return list(c)