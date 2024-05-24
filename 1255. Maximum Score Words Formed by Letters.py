from collections import Counter
from typing import List
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def word_score(word):
            return sum(score[ord(c) - ord('a')] for c in word)
        
        def can_form_word(word, letter_count):
            word_count = Counter(word)
            for c in word_count:
                if word_count[c] > letter_count[c]:
                    return False
            return True
        
        def helper(index, letter_count):
            if index == len(words):
                return 0
            
            # Option 1: Exclude the current word
            max_score = helper(index + 1, letter_count)
            
            # Option 2: Include the current word, if possible
            if can_form_word(words[index], letter_count):
                new_letter_count = letter_count - Counter(words[index])
                max_score = max(max_score, word_score(words[index]) + helper(index + 1, new_letter_count))
            
            return max_score
        
        letter_count = Counter(letters)
        return helper(0, letter_count)
