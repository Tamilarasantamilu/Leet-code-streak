class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7  # Modulus to prevent overflow
        stack = []       # Stack to keep track of elements and indices
        total_sum = 0    # Total sum of minimums of subarrays
        arr_length = len(arr)  # Length of the array

        for index, value in enumerate(arr):
            # Pop elements from stack if current value is less or equal
            while stack and value <= stack[-1][1]:
                prev_index, prev_value = stack.pop()
                left_count = prev_index - stack[-1][0] if stack else prev_index + 1
                right_count = index - prev_index
                total_sum += left_count * right_count * prev_value
                total_sum %= MOD
            stack.append((index, value))

        # Process remaining elements in the stack
        while stack:
            prev_index, value = stack.pop()
            left_count = prev_index - stack[-1][0]  if stack else prev_index + 1
            right_count = arr_length - prev_index
            total_sum += left_count * right_count * value
            total_sum %= MOD
        return total_sum
