class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Greedy algorithm

        # Start from left or 0th index of the string
        # Trying to ensure that the new stack has elements in ascending order from left to right, 
        # to reduce the overall value of the final number
       
        # 1. Add digit to a stack if current digit is greater than the last existing digit in stack

        # 2. If current digit is smaller than the last existing digit in stack, keep popping stack elements until 
        #    current digit is greater than the last element in stack, stack is not empty and k value condition is not met, 
        # 3. and then add the current digit
        
        if k >= len(num):
            return "0"
            
        stack = []
        for i in num:
            while stack and k > 0 and stack[-1] > i: # 2
                k-=1
                stack.pop()

            stack.append(i) # 1, 3

        # For situations when all digits are in ascending order, nothing may be removed, or when k > 0,
        # for such situations we can remove last k characters
        # lstrip to remove any leading zeros
        stack= stack[  : len(stack) - k   ] 
        strstack= "".join(stack).lstrip("0")

        return strstack if  strstack else "0"
