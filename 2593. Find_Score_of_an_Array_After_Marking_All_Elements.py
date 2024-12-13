import heapq

class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        min_heap = []
        marked = [False] * n  # To keep track of marked elements
        
        # Populate the heap with (value, index) pairs
        for i, num in enumerate(nums):
            heapq.heappush(min_heap, (num, i))
        
        score = 0
        
        while min_heap:
            value, idx = heapq.heappop(min_heap)
            
            # Skip if the element is already marked
            if marked[idx]:
                continue
            
            # Add to the score
            score += value
            
            # Mark the chosen element and its adjacent elements
            marked[idx] = True
            if idx > 0:
                marked[idx - 1] = True
            if idx < n - 1:
                marked[idx + 1] = True
        
        return score  
