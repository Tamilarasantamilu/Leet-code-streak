class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        c=permutations(nums,n)
        for i in c:
            ans.append(list(i))
        return ans