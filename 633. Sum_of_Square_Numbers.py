class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        dict = {}
        for i in range(int(c**0.5) + 1):
            dict[i * i] = 1
        for i in dict:
            if c - i in dict:
                return True
        return False
