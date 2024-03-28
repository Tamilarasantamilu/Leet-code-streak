class Solution:
  def maxSubarrayLength(self, nums: List[int], k: int) -> int:
    
    count = collections.Counter()

    l = 0
    answer = 0
    for r, num in enumerate(nums):
      count[num] += 1
      while count[num] == k + 1:
        count[nums[l]] -= 1
        l += 1
      answer = max(answer, r - l + 1)

    return answer
