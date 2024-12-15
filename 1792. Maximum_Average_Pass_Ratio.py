class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        def extra_pass_ratio(pass_count, total_count):
            return (pass_count + 1) / (total_count + 1) - pass_count / total_count

        # Create a max-heap using negative values since heapq is a min-heap in Python
        max_heap = []
        for pass_count, total_count in classes:
            heapq.heappush(max_heap, (-extra_pass_ratio(pass_count, total_count), pass_count, total_count))

        # Allocate extra students
        for _ in range(extraStudents):
            _, pass_count, total_count = heapq.heappop(max_heap)
            pass_count += 1
            total_count += 1
            heapq.heappush(max_heap, (-extra_pass_ratio(pass_count, total_count), pass_count, total_count))

        # Calculate the total average ratio
        ratio_sum = 0
        while max_heap:
            _, pass_count, total_count = heapq.heappop(max_heap)
            ratio_sum += pass_count / total_count

        return ratio_sum / len(classes)
