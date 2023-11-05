class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        k = min(k, len(arr) - 1)
        wins = 0
        curr = arr[0]
        i = 0
        A = len(arr)
        while wins < k:
            i = (i + 1) % A
            if arr[i] > curr:
                curr = arr[i]
                wins = 0
            wins += 1
        return curr
