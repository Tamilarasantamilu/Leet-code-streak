class Solution:
    def getLucky(self, s: str, k: int) -> int:
        import string

        alphabets = string.ascii_lowercase

        convert = ""
        for ch in s:
            convert += str(alphabets.index(ch)+1)
            
        while k > 0:
            total = 0
            for i in range(len(convert)):
                total += int(convert[i])
                
            k -= 1
            convert = str(total)


        return total
