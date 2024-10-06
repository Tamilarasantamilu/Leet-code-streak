class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Split the sentences into words
        smaller_str = sentence2.split(' ')
        larger_str = sentence1.split(' ')

        # Ensure smaller_str is indeed the smaller sentence
        if len(sentence1) < len(sentence2):
            smaller_str = sentence1.split(' ')
            larger_str = sentence2.split(' ')

        # Count the occurrences of each word in both sentences
        small_counter = Counter(smaller_str)
        large_counter = Counter(larger_str)

        # Get the lengths of both sentences
        len_smaller_str = len(smaller_str)
        len_larger_str = len(larger_str)

        # Check if larger sentence has at least the same number of each word as the smaller sentence
        for word, count in small_counter.items():
            if large_counter[word] < count:
                return False  # Not enough of the word in the larger sentence

        # Initialize a counter for matched words from the start
        matched_words_target = len_smaller_str

        # Check for matching words from the beginning of both sentences
        for i in range(matched_words_target):
            if smaller_str[i] == larger_str[i]:
                matched_words_target -= 1  # Found a match
            else:
                break  # No longer matching, exit loop

        # If all words in smaller sentence match from the start
        if matched_words_target == 0:
            return True

        # Check for matching words from the end of both sentences
        for i in range(matched_words_target):
            if smaller_str[len_smaller_str - 1 - i] == larger_str[len_larger_str - 1 - i]:
                matched_words_target -= 1  # Found a match
            else:
                break  # No longer matching, exit loop

        # If all remaining words match from the end
        if matched_words_target == 0:
            return True

        # If we reach here, sentences are not similar
        return False
