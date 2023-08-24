class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        curr = []
        char_count = 0
        
        for word in words:
            # check if adding this word exceeds the max width
            if char_count + len(curr) + len(word) > maxWidth:
                # calculate the number of spaces needed to evenly distribute
                # the extra spaces between words
                num_spaces = maxWidth - char_count
                if len(curr) == 1:
                    # if there is only one word, left justify it and pad the
                    # rest of the line with spaces
                    result.append(curr[0] + ' ' * num_spaces)
                else:
                    # distribute the extra spaces between words as evenly as possible
                    num_gaps = len(curr) - 1
                    space_per_gap = num_spaces // num_gaps
                    extra_spaces = num_spaces % num_gaps
                    line = ''
                    for i in range(num_gaps):
                        line += curr[i] + ' ' * space_per_gap
                        if extra_spaces > 0:
                            line += ' '
                            extra_spaces -= 1
                    line += curr[-1]
                    result.append(line)
                
                # start a new line with the current word
                curr = [word]
                char_count = len(word)
            else:
                # add the current word to the current line
                curr.append(word)
                char_count += len(word)
        
        # handle the last line, which is always left justified
        last_line = ' '.join(curr)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)
        
        return result

def _driver():
    test_cases = [
        (["This", "is", "an", "example", "of", "text", "justification."], 16),
        (["What","must","be","acknowledgment","shall","be"], 16),
        (["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20),
    ]
    for words, maxWidth in test_cases:
        ret = Solution().fullJustify(words, maxWidth)
        print(ret)

if __name__ == '__main__':
    _driver()