class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        else:
            i = word.index(ch)
            fs = word[0:i + 1]
            r = fs[::-1]
            ss = word[i + 1:]
            return r + ss
