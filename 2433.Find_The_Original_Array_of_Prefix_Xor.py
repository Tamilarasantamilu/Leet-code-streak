class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        x = []

        for i in range(0,len(pref)):
            if i==0:
                x.append(pref[i])
            else:
                x.append(pref[i]^pref[i-1])

        return x
