class Solution:
    def countStudents(self, st: List[int], sa: List[int]) -> int:
        ct = Counter(st)
        for s in sa:
            if ct[s] > 0: 
                ct[s] -= 1
            else:
                return ct.total()
        return 0
