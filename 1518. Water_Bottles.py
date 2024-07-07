# Platform: leetcode.com
# No. 1518. Water Bottles
# Link: https://leetcode.com/problems/water-bottles/
# Difficulty: Easy
# Dev: Chumicat
# Date: 2020/11/1
# Submission: https://leetcode.com/submissions/detail/415551474/
# (Time, Space) Complexity : O(1), O(1)
# For n = numBottles and m = numExchange
# 
# Let's list some situation of (n, m):
#   1,2 = 1  1,3 = 1  1,4 = 1
#   2,2 = 3  2,3 = 2  2,4 = 2
#   3,2 = 5  3,3 = 4  3,4 = 3
#   4,2 = 7  4,3 = 5  4,4 = 5
#   5,2 = 9  5,3 = 7  5,4 = 6
# 
# 1. We can find that while the rest count of the bottle is equal to m perfectly
#      we will get a boost in the result and rest one bottle
#      which means that for each m-1 round, we will get a boost
# 2. For the first round, we didn't get one rest from the previous boost
#      So when we calculate the boost part of the result
#      the denominator will be subtracted by one
# 3. Finally, according to the two rule above, 
#      we get that we can get boost of (n-1)//(m-1)
#    The total count will be = n + (n-1)//(m-1)
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles-1) // (numExchange-1)
