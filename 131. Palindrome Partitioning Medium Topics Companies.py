class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        path=[]

        def help(index):
            if index==len(s):
                res.append(path[:])
                return
            for i in range(index,len(s)):
                if palin(s,index,i):
                    path.append(s[index:i+1])
                    help(i+1)
                    path.pop()

        def palin(s,start,end):
            while start<=end:
                if s[start]!=s[end]:
                    return False
                start+=1
                end-=1
            return True
        help(0)
        return res
