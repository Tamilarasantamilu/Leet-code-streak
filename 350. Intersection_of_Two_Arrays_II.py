from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Create a Counter for nums1 to count the occurrences of each element
        counts = Counter(nums1)
        result = []

        # Iterate through nums2 and collect the common elements
        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1

        return result 
