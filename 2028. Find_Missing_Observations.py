class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        roll_sum = sum(rolls)
        missing_sum = ((m+n)*mean) - roll_sum
        i = 0
        res = []
        while missing_sum > 0 and n >0:
            res.append(missing_sum//n)
            if res[i] > 6 or res[i] < 1:
                return []
            missing_sum -= res[-1]
            n -= 1
            i += 1
        return res
