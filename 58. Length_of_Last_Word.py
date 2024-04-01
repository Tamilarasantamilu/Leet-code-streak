class Solution(object):
    def lengthOfLastWord(self, s):
        res=s.split()
        return (len(res[-1]))
        
