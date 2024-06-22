class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        a, c, t, s = 0, 0, 0, 0
        for i in range(len(nums)):
            if nums[i] & 1 != 0:
                t += 1
            if t == k:
                c = 0
                while t == k:
                    if nums[a] & 1 != 0:
                        t -= 1
                    c += 1
                    a += 1
            s += c
        return s
