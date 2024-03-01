class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
       counts = Counter(s)
       return '1' * (counts['1'] - 1) + '0' * (counts['0']) + '1'
