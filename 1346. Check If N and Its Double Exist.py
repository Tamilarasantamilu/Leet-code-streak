from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        
        for num in arr:
            # Check if double or half exists in the set
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            # Add the current number to the set
            seen.add(num)
        
        return False

        
