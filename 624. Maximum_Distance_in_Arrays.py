class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        md = 0
        omin = arrays[0][0]
        omax = arrays[0][-1]
        n = len(arrays)
        for i in range(1,n):
            cmin = arrays[i][0]
            cmax = arrays[i][-1]
            md = max(md,abs(cmax-omin),abs(omax-cmin))
            omin = min(omin,cmin)
            omax = max(omax,cmax)
        return md
