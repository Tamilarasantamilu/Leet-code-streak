class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        end = -float('inf')
        intervals = sorted(intervals, key = lambda x:x[1])
        for interval in intervals:
            if interval [0] >= end:
                res += 1
                end = interval[1]
        return len(intervals) - res 