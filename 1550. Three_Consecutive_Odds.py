from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # Iterate through the array up to the third last element
        for i in range(len(arr) - 2):
            # Check if the current element and the next two elements are odd
            if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2] % 2 == 1:
                return True
        return False

# Example usage:
# solution = Solution()
# print(solution.threeConsecutiveOdds([2,6,4,1]))  # Output: false
# print(solution.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))  # Output: true
