class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        d = sentence.split(" ")
        for i in range(len(d)):
            if searchWord == d[i][0:len(searchWord)]:
                return i+1
        return -1
        
