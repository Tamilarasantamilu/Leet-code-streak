class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    tails = [0] * n # initialize tails array with 0
    size = 0
    for num in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if tails[m] < num:
                i = m + 1
            else:
                j = m
        tails[i] = num
        size = max(i + 1, size)
    return size
