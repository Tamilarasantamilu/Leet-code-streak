class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase1:Intersection point
        fast = slow = nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        # Phase 2: Find the cycle entrance
        slow = nums[0]
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]
        return slow
