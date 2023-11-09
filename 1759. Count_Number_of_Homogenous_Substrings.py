class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD=10**9+7
        res=0
        cnt=1
        ans=[]
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                cnt+=1
            else:
                ans.append((cnt*(cnt+1)//2)%MOD)
                cnt=1
        ans.append((cnt*(cnt+1)//2)%MOD)
        res=sum(ans)%MOD
        return res        
