class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sum = [0] * (n + 1)
        
        curr_sum = 0
        for i in range(n):
            curr_sum += nums[i]
            sum[i + 1] = curr_sum
        
        deq = deque()
        min_length = n + 1
        
        for i in range(n + 1):
            while deq and sum[i] >= sum[deq[0]] + k:
                min_length = min(min_length, i - deq[0])
                deq.popleft()
                
            while deq and sum[i] <= sum[deq[-1]]:
                deq.pop()
                
            deq.append(i)
            
        return min_length if min_length <= n else -1
