class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if (sx == fx and sy == fy):
            return t != 1
        dx = abs(sx - fx)
        dy = abs(fy - sy)
        return t >= max(dy, dx)
