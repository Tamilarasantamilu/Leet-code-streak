class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.ans = []
        def word(start,end,lst):
            if end==len(s):
                if start==end:
                    self.ans.append(" ".join(lst))
                return
            if s[start:end+1] in wordDict:
                lst.append(s[start:end+1])
                word(end+1,end+1,lst)
                lst.pop()
            word(start,end+1,lst)
        word(0,0,[])
        return self.ans
