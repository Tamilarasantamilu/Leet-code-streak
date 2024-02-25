
class UnionFind:
    def __init__(self, n):
        self.roots = [i for i in range(n)]
        self.ranks = [1] * n
        self.components = n

    def find(self, x):
        if self.roots[x] != x:
            self.roots[x] = self.find(self.roots[x])
        return self.roots[x]

    def union(self, x, y):
        X = self.find(x)
        Y = self.find(y)
        if X == Y: return False
        if self.ranks[X] < self.ranks[Y]:
            self.roots[X] = Y
        elif self.ranks[Y] < self.ranks[X]:
            self.roots[Y] = X
        else:
            self.roots[X] = Y
            self.ranks[Y] += 1
        self.components -= 1
        return True

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        MAX_NUM = max(nums)
        sieve = [0] * (MAX_NUM + 1)
        for i in range(2, len(sieve)):
            if sieve[i] != 0:
                continue
            for j in range(i + i, MAX_NUM + 1, i):
                if sieve[j] == 0:
                    sieve[j] = i
    
        uf = UnionFind(len(nums))
        primes = defaultdict(list)
        for i, v in enumerate(nums):
            while v != 1:
                factor = sieve[v] if sieve[v] != 0 else v
                primes[factor].append(i)
                while v % factor == 0:
                    v //= factor
        for val in primes.values():
            for i in range(len(val) - 1):
                uf.union(val[i], val[i + 1])
        return uf.components == 1
