class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        def numToBits(x: int) -> List[int]:
            bin_arr = []
            while x != 0:
                bin_arr.insert(0, x%2)
                x = int(x/2)
            return bin_arr

        start_bin = numToBits(start)
        goal_bin = numToBits(goal)

        while len(start_bin) > len(goal_bin):
            goal_bin.insert(0,0)
        while len(start_bin) < len(goal_bin):
            start_bin.insert(0,0)
        
        count = 0
        for i in range(len(goal_bin)):
            if goal_bin[i] != start_bin[i]:
                count+=1

        return count
