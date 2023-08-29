class Solution:
    def bestClosingTime(self, customers: str) -> int:
        result = mx = curr = 0
        
        for i, x in enumerate(customers):
            curr += 1 if x == 'Y' else -1
            if curr > mx:
                mx = curr
                result = i+1
        return result