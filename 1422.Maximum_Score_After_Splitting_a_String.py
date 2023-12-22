class Solution:
    def maxScore(self, s: str) -> int:
        
        def count(zero,one):
            cone=0
            czero=0
            for i in one:
                if i=='1':
                    cone+=1
            for i in zero:
                if i == '0':
                    czero+=1
            if czero==0:
                return  cone-1
            # print(f"{czero}+{cone}={czero+cone}")
            return czero+cone

        left=''
        p=[]
        right=''
        for i in range(len(s)):
            left=s[:i]
            right=s[i:]
            # print(f"one is {right},zero is left = {left}")
            p.append(count(left,right))
        return max(p) 
