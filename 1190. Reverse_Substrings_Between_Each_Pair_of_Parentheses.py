class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        current_string = []

        for char in s:
            if char == '(':
                # Push the current string to stack and start a new one
                stack.append(current_string)
                current_string = []
            elif char == ')':
                # Reverse the current string
                current_string.reverse()
                # Pop the stack and append the reversed string
                current_string = stack.pop() + current_string
            else:
                # Append the character to the current string
                current_string.append(char)

        return ''.join(current_string)
