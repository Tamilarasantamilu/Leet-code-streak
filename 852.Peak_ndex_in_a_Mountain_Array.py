class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                i+=1
            else:
                break
        return i