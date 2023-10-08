class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        @lru_cache(None)
        def r(i,j):
            if i==0 or j==0:
                return 0
            else:
                return max(nums1[i]*nums2[j]+r(i+1,j+1),r(i,j+1),r(i+1,j))
        best = -1000000000
        for i in range(-len(nums1),0):
            for j in range(-len(nums2),0):
                c=nums1[i]*nums2[j]+r(i+1,j+1)
                if c>best:
                    best=c
        return best

        
