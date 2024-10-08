class Solution:
    def minSwaps(self, s: str) -> int:
        closebr=0
        openbr=0
        for char in s:
            if char=='[':
                openbr+=1
            elif char==']':
                if openbr>0:
                    openbr-=1
                else:
                    closebr+=1
        return (closebr+1)//2 
