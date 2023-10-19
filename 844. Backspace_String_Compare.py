class Solution:
    # O(n) time | O(n) space
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.helper(s) == self.helper(t)

    def helper(self, string: str) -> str:
        stack = []
        for char in string:
            if char != "#":
                stack.append(char)
            elif len(stack) > 0:
                stack.pop()
        return "".join(stack)
