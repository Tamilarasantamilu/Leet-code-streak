class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        res = {key: val for key, val in sorted(d.items(), key = lambda ele: ele[1], reverse = True)}
        s=""
        for i in res:
            s=s+(i*res[i])
        return s
