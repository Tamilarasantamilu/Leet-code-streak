class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def timeToMinutes(time: str) -> int:
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes
        
        
        minutes = sorted(timeToMinutes(t) for t in timePoints)
        
        
        min_diff = float('inf')
        
        
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
        
        
        min_diff = min(min_diff, (minutes[0] + 1440) - minutes[-1])
        
        return min_diff
        
