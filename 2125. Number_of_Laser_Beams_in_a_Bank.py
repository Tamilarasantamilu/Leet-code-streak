class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total=0
        arr=0
        for x in bank:
            n = x.count('1')
            if n == 0:
                continue
            total += arr * n
            arr = n
        return total
