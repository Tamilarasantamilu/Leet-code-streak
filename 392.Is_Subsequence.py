class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l1=l2=0
        temp=''
        while l1<len(s) and l2<len(t):
            if s[l1]==t[l2]:
                temp+=s[l1]
                l1+=1
                l2+=1
            elif s[l1]!=t[l2]:
                l2+=1
        print(temp)
        if temp==s:
            return True
        return False
