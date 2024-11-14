from typing import List

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        start = 1
        end = max(quantities)
        
        while start <= end:
            mid = start + (end - start) // 2
            # Calculate the total number of stores needed for the current mid value
            total = sum((element // mid) + (1 if (element % mid) > 0 else 0) for element in quantities)
            
            if total <= n:
                # If the number of stores needed is less than or equal to the available stores,
                # we try to minimize the maximum by reducing mid
                end = mid - 1
            else:
                # If the number of stores needed is greater than the available stores,
                # we need to increase mid to reduce the number of stores needed
                start = mid + 1
        
        # The smallest value for which total <= n is `start`
        return start
