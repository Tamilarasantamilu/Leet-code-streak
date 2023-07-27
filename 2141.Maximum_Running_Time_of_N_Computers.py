class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        summ = sum(batteries)
        
        batteries.sort()
        
        while batteries[-1] > summ // n:
            n -= 1
            summ -= batteries.pop()

        return summ // n