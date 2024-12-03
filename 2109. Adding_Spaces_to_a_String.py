class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        p1 = 0
        for i in range(len(s)):
            p2 = spaces[p1]
            if i == p2:
                ans += " " + s[i] 
                if p1 < len(spaces)-1:
                    p1 += 1
            else:
                ans += s[i]  
        return (ans)
