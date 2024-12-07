class Solution:
    def f(self,arr,x):
        cnt = 0
        for i in range(len(arr)):
            cnt +=  math.ceil(arr[i]/x) - 1
        return cnt

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l = 1
        r = max(nums)
        ans=0
        while l <= r:
            mid = l + (r-l) // 2
            val = self.f(nums,mid)
            if val <= maxOperations:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
