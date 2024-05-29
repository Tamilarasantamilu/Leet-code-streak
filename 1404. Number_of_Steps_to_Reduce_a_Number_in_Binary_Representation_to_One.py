class Solution:
    def numSteps(self, s: str) -> int:
        def count(number):
            counter = 0
            if number == 1:
                return 0
            if number % 2 == 0:
                number = number // 2
                counter += 1
                return counter + count(number)
            else:
                number = number + 1
                counter += 1
                return counter + count(number)
        number = int(s,2)
        return count(number)
        
