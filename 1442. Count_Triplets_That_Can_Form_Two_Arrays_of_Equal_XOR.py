class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefix_xor = [0] * (n + 1)
        
        # Compute prefix_xor
        for i in range(n):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]
        
        count = 0
        xor_map = {}
        
        # Iterate to find valid (i, j, k)
        for j in range(n):
            for k in range(j + 1, n):
                if prefix_xor[j] == prefix_xor[k + 1]:
                    count += k - j
        
        return count
