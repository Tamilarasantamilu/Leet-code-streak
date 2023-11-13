class Solution:
        def sortVowels( self,s):
            intial = list(s)
            vowels = {}
            regex = '^[aeiouAEIOU]'
            for letter in range(0, len(s)):
                if (re.search(regex, s[letter])):
                    vowels[letter] = s[letter]
            sorter = list(vowels.values())
            sorter.sort()
            called = 0
            for letter in vowels:
                intial[letter] = sorter[called] #Here letter comes as Key which is numeric'
                called += 1
            final = ''.join(intial)
            return final
