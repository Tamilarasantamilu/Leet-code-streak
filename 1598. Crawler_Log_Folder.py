class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0

        for x in logs:
            if x == './':
                continue
            elif x == '../':
                if not res:
                    continue
                res -= 1
            else:
                res += 1
        return res
