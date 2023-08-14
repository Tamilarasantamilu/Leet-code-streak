class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # An empty list to store the words in the str
        list = []
        # Split the words using the space delimeter
        words = s.split(' ')
        # In case of spaces before, in or after the array filter them out
        for i in words:
            if i is not '':
                # append the words on the list
                list.append(i)
        #print(list)
        # Slice the last word on the list
        last_word = list[-1]
        # Return the length of the last word
        return (len(last_word))