class Solution:
    def minSteps(self, n: int) -> int:
        if n ==  1: 
            return 0
        operations = 0  *#to keep the track of number of operations*
        divisor = 2 *#taking divisor as 2,in order to see it n is divisible and returns 3*
        while n > 1:  *#if n is greater than 1,it enters the inner loop*
            while n % divisor == 0: *#inner loop makes sure that n is divisible by the divisor*
                operations += divisor *#if so,operations is counted to divisor*
                n //= divisor *#n is reduced by divided it by divisor*
            divisor += 1

        return operations
