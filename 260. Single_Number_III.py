class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        x=[]
        for j in d:
            if d[j]==1:
                x.append(j)
        return x
