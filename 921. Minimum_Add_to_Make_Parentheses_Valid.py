class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        count=0
        for c in s:
            if c=='(':
                stack.append(c)
            else:
                if not stack:
                    count+=1
                else:
                    stack.pop()
        return count+len(stack)
        
