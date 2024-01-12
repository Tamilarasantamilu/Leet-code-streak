class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)
        count1=0
        count2=0
        vowel= ['a','e','i','o','u','A','E','I','O','U']
        if n%2==0:
            s1=s[0:n//2]
            s2=s[n//2:n]
            for x in s1:
                if x in vowel:
                    count1+=1
            for y in s2:
                if y in vowel:
                    count2+=1
        if count1 == count2:
            return True
        else:
            return False
