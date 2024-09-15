class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Result to store the maximum length of the substring
        max_len = 0
        
        # To store the first occurrence of each mask (32 possible states for 5 vowels)
        prefix_index = [-1] * 32

        # Initializing for the empty prefix case
        prefix_index[0] = 0  
        
        # Mapping vowels to their respective bit positions
        vowel_to_bit = {vowel: 1 << i for i, vowel in enumerate("aeiou")}
        
        # To track the current mask of vowels
        mask = 0  
        
        # Traverse the string character by character. Start index at 1 to handle initial prefix case
        
        for i, ch in enumerate(s, 1):  
            # If the character is a vowel, update the mask
            if ch in vowel_to_bit:
                mask ^= vowel_to_bit[ch]

            # If this mask has been seen before, update max_len
            if prefix_index[mask] != -1:
                max_len = max(max_len, i - prefix_index[mask])
            else:
                prefix_index[mask] = i
        
        return max_len
