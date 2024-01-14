from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        counter1 = Counter(word1)
        counter2 = Counter(word2)

        if set(word1) != set(word2):
            return False

        return sorted(counter1.values()) == sorted(counter2.values())
