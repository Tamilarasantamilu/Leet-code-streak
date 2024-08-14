class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        left, right = 0, nums[-1] - nums[0]

        def count_pairs(mid):
            """ returns the number of pairs up to the mid part
            """
            count, left = 0, 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1

                count += right - left
            return count
        
        while left < right:
            mid = (left + right) // 2

            if count_pairs(mid) < k:
                left = mid + 1
            else:
                right  = mid
        return left
