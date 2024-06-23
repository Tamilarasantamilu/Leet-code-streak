from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        a,r=0,0
        max_deque = deque()
        min_deque = deque()
        for b in range(len(nums)):
            while max_deque and nums[max_deque[-1]] < nums[b]:
                max_deque.pop()
            max_deque.append(b)
            while min_deque and nums[min_deque[-1]] > nums[b]:
                min_deque.pop()
            min_deque.append(b)
            maxi=nums[max_deque[0]]
            mini=nums[min_deque[0]]
            while maxi-mini>limit:
                a+=1
                if max_deque[0]<a:
                    max_deque.popleft()
                if min_deque[0]<a:
                    min_deque.popleft()
                
                if max_deque:
                    maxi=nums[max_deque[0]]
                if min_deque:
                    mini=nums[min_deque[0]]
            r = max(r, b - a + 1)
        return r
