class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ma = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:   # if stack is empty
                    stack.append(i)
                else:
                    ma = max(ma, i - stack[-1])
        return ma
