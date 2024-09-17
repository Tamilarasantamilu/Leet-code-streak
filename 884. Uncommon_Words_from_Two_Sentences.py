class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Splitting the words and storing it in variable word_2
        word_s1 = s1.split()
        word_s2 = word_s1 + s2.split()

        # Counting number of words
        count = Counter(word_s2)

        # Returning only words which appears only once
        return [word for word in count if count[word] == 1]
