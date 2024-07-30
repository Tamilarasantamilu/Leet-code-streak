class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        a_count = sum(1 for ch in s if ch == "a")  # Total number of 'a's in the string
        b_count = 0  # Counter for the number of 'b's encountered
        min_deletions = n  # Initialize min_deletions to the length of the string
        
        for ch in s:
            if ch == "a":
                a_count -= 1  # We've encountered one 'a', so decrease the count of remaining 'a's
            # Calculate the current minimum deletions: remaining 'a's + encountered 'b's
            min_deletions = min(min_deletions, a_count + b_count)
            if ch == "b":
                b_count += 1  # We've encountered one 'b', so increase the count of 'b's
            
        return min_deletions  # Return the minimum deletions required to balance the string
