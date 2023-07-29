class Solution:
    def soupServings(self, n: int) -> float:
        if n>4450: return 1
        @cache
        def dfs(a,b):
            if a<=0:
                if b<=0: return 0.5 
                else: return 1 
            elif b<=0: return 0 
            return 0.25 * (dfs(a-100,b) + dfs(a-75,b-25) + dfs(a-50,b-50) + dfs(a-25,b-75))
        return dfs(n,n)