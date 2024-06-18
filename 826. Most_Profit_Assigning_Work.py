class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        if max(worker) < min(difficulty): return 0
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        
        ans = j = maxp = 0
        for w in worker:
            while j < len(jobs) and jobs[j][0] <= w:
                maxp = max(maxp, jobs[j][1])
                j+=1
            ans += maxp
        return ans
