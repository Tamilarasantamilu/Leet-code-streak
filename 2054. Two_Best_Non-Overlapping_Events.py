class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        f = [events[-1][2]] * n
        t_start = [events[-1][0]] * n
        for i in range(n-2,-1,-1):
            f[i] = max(f[i+1], events[i][2])
            t_start[i] = events[i][0]
        events.sort(key = lambda x:x[1])
        ans = max([a[2] for a in events])
        p = 0
        for t1, t2, val in events:
            while p < n and t_start[p] <= t2:
                p += 1
            if p<n:
                ans = max(ans, val + f[p])
        return ans
