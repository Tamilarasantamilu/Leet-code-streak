class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        farthest = max(max(left,default=0),n-min(right,default=n))
        return farthest
        
