import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Create a max heap based on character counts
        max_heap = []
        if a > 0:
            heapq.heappush(max_heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(max_heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(max_heap, (-c, 'c'))

        result = []

        while max_heap:
            first_count, first_char = heapq.heappop(max_heap)
            first_count = -first_count  # Convert back to positive

            # Check the last two characters in the result to avoid three in a row
            if len(result) >= 2 and result[-1] == result[-2] == first_char:
                if not max_heap:  # If we can't use any other character
                    break
                second_count, second_char = heapq.heappop(max_heap)
                second_count = -second_count  # Convert back to positive

                # Use the second character
                result.append(second_char)
                second_count -= 1
                if second_count > 0:
                    heapq.heappush(max_heap, (-second_count, second_char))

                # Push the first character back to the heap
                heapq.heappush(max_heap, (-first_count, first_char))
            else:
                # Use the first character
                result.append(first_char)
                first_count -= 1
                if first_count > 0:
                    heapq.heappush(max_heap, (-first_count, first_char))

        return ''.join(result)
