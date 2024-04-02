class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        l1 = []
        l2 = []
        for i in range(len(s)):
            l1.append(s.index(s[i]))
            l2.append(t.index(t[i]))

        return (l1==l2)
        
