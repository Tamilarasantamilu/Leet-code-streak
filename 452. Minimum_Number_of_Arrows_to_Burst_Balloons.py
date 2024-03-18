class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Step 1: Sort balloons by ending points
        points.sort(key=lambda x: x[1])

        arrows = 1  # Initialize arrow count to 1 (at least one arrow is needed)
        end = points[0][1]

        # Step 3: Iterate through sorted balloons
        for xstart, xend in points:
            # Balloon does not overlap with the previous one
            if xstart > end:
                arrows += 1
                end = xend  # Update the ending point

        return arrows  # Step 4: Return the number of arrows
