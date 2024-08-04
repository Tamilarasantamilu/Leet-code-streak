class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res=[]
        mod=1e9 +7
        for i in range(len(nums)):
            sum=0
            for j in range (i,len(nums)):
                sum+=nums[j]
                res.append(sum)
        res.sort()
        presum=[]
        presum.append(res[0])
        for i in range(1,len(res)):
            presum.append(res[i]+presum[i-1])
        ans=presum[right-1]-presum[left-1]+res[left-1]
        return int(ans%mod)

        
