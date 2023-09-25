class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if t[i] != s[i]:
                return t[i]   
        return t[-1]
