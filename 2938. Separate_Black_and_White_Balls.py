class Solution:
    def minimumSteps(self, s: str) -> int:
        black_balls_counter = 0
        current = 0
        total_swaps = 0
        n = len(s)
        while current < n:
            if s[current] == "1":  # black ball
                black_balls_counter += 1
            else:
                total_swaps += black_balls_counter
            current += 1
        
        return total_swaps
