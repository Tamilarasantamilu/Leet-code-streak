class Solution:
    def reverseWords(self, s: str) -> str:
        result = ''
        str_list = s.split()
        n = len(str_list)
        for i in range(n):
            temp = self.reverseWord(str_list[i])
            result += temp
            result += ' '
        result = result[:len(result) - 1]
        return result
    def reverseWord(self, word: str) -> str:
        return word[::-1]
