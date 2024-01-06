class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        S = len(startTime)
        joins = sorted(zip(startTime, endTime, profit))
        cache = {}
        def next_job(time, i):
            l, r = i + 1, S - 1
            res = S
            while l <= r:
                p = (l + r) // 2
                if joins[p][0] >= time:
                    res = p
                    r = p - 1
                else:
                    l = p + 1
            return res
        
        def dp(index):
            if index == S:
                return 0
            if index in cache:
                return cache[index]
            cache[index] = max(
                joins[index][2] + dp(next_job(joins[index][1], index)), 
                dp(index + 1)
            )
            return cache[index]
        return dp(0)
