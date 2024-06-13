class Solution:
    def minMovesToSeat(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = sorted(arr1)
        arr2 = sorted(arr2)
        t = 0
        for i in range(len(arr1)):
            t += abs(arr1[i] - arr2[i])
        return t
