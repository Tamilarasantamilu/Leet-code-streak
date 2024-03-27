class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        left = 0
        res=0
        product =1
        for i in range(len(nums)):
            product*=nums[i]
            if product >=k:
                while product>=k and left<=i:
                    product/=nums[left]
                    left+=1
            res+=i-left+1
        return res
