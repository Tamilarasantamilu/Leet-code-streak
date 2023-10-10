class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N= len(nums)
        arr=sorted(set(nums))
        A=len(arr)
        res=N-1
        l=0

        for i in range(A):
            l_b=arr[i]-N+1
            while arr[l]< l_b:
                l +=1
            res=min(res,N-(i-l+1))
        return res
        
