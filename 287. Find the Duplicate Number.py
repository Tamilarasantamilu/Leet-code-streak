class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for j in d:
            if d[j]>1:
                return j
