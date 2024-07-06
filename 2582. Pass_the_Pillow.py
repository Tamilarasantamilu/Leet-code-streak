class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        complete_rounds, remaining_time = divmod(time, n - 1)
        
        if complete_rounds % 2 == 0:
            # Pillow is moving from start to end
            return remaining_time + 1
        else:
            # Pillow is moving from end to start
            return n - remaining_time
