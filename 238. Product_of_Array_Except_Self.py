# input: int array 
# output: int array - each index contains the product of every number in input array except for its own index value. 
# example: 
    # 1   2   3    4 
    # 24  12  8   6 
# cases: 
    # nums length between 2 an 10^5 
    # 1              2   3    4 
    # 1              3    4 
    # 1   2          4 
    # 1   2   3      1  
    # 24  12  8   6 
    # prefix - [1  1  2 6]
    # postfix -[24 12 4 1]
# method: 
    # create 2 arrays, one array contains the prefix values multiplied together, one array contains the postfix values
    # multiply each corresponding index value together to get the solution 
# [1 2 3 4 ]
# [24 12 8 6 ]
# postfix: 24
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = 1 
        for i in range(len(nums)): 
            result[i] = prefix 
            prefix *= nums[i]
        postfix = 1 
        for i in range(len(nums) - 1, -1, -1): 
            result[i] *= postfix 
            postfix *= nums[i]
        return result 
