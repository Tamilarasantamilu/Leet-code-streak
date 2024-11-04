class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0
        J = len(word)
        
        while i < J:
          
            char = word[i]
            
            count = 0
            while i < J and word[i] == char and count < 9:
                count += 1
                i += 1
            
            comp += str(count) + char
        
        return comp
