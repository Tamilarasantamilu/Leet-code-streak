class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []
        res = []
        for i in range(len(nums)):
            if i<k-1:
                while len(window) and window[-1]<nums[i]:
                    window.pop(-1)
                window.append(nums[i])
            else:
                while len(window) and window[-1]<nums[i]:
                    window.pop(-1)
                window.append(nums[i])
                res.append(window[0])
                if nums[i-k+1]==window[0]:
                    window.pop(0)
        return res