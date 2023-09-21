import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
      combined_list = []
      modified_list = []
      combined_list.extend(nums1)
      combined_list.extend(nums2)
      mid = len(nums1)-1
      i, mid , j = 0, mid , mid+1
      while(i <= mid and j < len(combined_list)):
        if combined_list[i]>combined_list[j]:
          modified_list.append(combined_list[j])
          j+=1
        else:
          modified_list.append(combined_list[i])
          i+=1  
      if j == len(combined_list):
        for x in range(i, mid+1):
          modified_list.append(combined_list[x])
      else:
        for x in range(j, len(combined_list)):
          modified_list.append(combined_list[x])
      
      length = len(modified_list)
      if length%2 == 0:
        val = (modified_list[length//2]+modified_list[(length//2)-1])/2
      else:
        val = modified_list[(length//2)]
      return val
