class Solution:
    def pivotInteger(self, n: int) -> int:
        integers = list(range(1,n+1))
        if len(integers) == 1:
            return integers[0]
        
        left_sum = 0
        right_sum = sum(integers[1:])
        
        for index in range(1, len(integers)):
            left_sum += integers[index - 1]
            right_sum -= integers[index]
            
            if left_sum == right_sum:
                return integers[index]

        return -1

            
