
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if s & t are the same length 
        if len(s) != len(t): 
            return False 

        sStorage = dict()
        tStorage = dict()

        for i in range(len(s)): 
            sStorage[s[i]] = sStorage.get(s[i], 0) + 1
            tStorage[t[i]] = tStorage.get(t[i], 0) + 1
        
        return sStorage == tStorage


        
