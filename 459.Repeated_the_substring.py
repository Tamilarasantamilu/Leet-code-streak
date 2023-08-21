class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        stringlen=len(s)
        
        for i in range(0,len(s)//2):
            string=s[0:i+1]
            length=len(string)
            required=len(s)//length
            if(string*required==s):
                return True
        return False