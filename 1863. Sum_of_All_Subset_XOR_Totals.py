class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result=[]
        self.backtrack(result,0,[],nums)
        sum=0
        for i in range(len(result)):
            sum=sum+self.XOR(result[i])
        return sum
        #return result
    def backtrack(self,result,start,subset,nums):
        result.append(list(subset))
        for i in range(start,len(nums)):
            subset.append(nums[i])
            self.backtrack(result,i+1,subset,nums)
            subset.pop()
    def XOR(self,subset):
        ans=0
        for i in range(len(subset)):
            ans=ans^subset[i]
        return ans
