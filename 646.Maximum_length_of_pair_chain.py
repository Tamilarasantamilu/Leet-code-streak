class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])  # Sort pairs based on ending values
        c = 0
        end = float('-inf')  # Initialize the ending value to negative infinity

        for i in pairs:
            if i[0] > end:
                c+= 1
                end = i[1]

        return c