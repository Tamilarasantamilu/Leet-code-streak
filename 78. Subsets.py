class Solution:
    len_nums = 0
    q = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.q = []
        self.len_nums = len(nums)
        
        self.rec(nums, [], 0)
        
        return self.q
    
    def rec(self, nums, temp_list, i):
        self.q.append(temp_list)
        if self.len_nums == i:
            return;
        
        for j in range(i, self.len_nums):
            self.rec(nums, temp_list + [nums[j]], j+1)
