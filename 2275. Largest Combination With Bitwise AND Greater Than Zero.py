class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        position_count = {}
        for num in candidates:
            binary_str = bin(num)[2:]
            for i, bit in enumerate(binary_str[::-1]):
                if bit == '1':
                    position_count[i] = position_count.get(i, 0) + 1
           
        return max(position_count.values())

            
