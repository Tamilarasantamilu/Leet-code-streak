class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        maxlength=0
        start=0
        curcost=0
        for end in range(len(s)):
            curcost+=abs(ord(s[end])-ord(t[end]))
            while curcost>maxCost:
                curcost -= abs(ord(s[start])-ord(t[start]))
                start+=1
            maxlength=max(maxlength,end-start+1)
        return maxlength        
