class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res1=[]
        res2=[]
        for i in nums:
            if i%2==0:
                res1.append(i)
            else:
                res2.append(i)
        return res1+res2
