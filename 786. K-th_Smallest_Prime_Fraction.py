class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:

        left = 0
        right = left + 1
        fraction_dict = {}

        while left < len(arr):

            while right < len(arr):
                fraction_dict[arr[left], arr[right]] = arr[left]/arr[right]
                right += 1

            left += 1
            right = left + 1

        sorted_dict = sorted(fraction_dict.items(), key=lambda x:x[-1])

        return sorted_dict[k-1][0]
