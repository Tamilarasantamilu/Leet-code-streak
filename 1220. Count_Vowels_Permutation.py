class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        transitions = {
            'a': ['e'],
            'e': ['a', 'i'],
            'i': ['a', 'e', 'o', 'u'],
            'o': ['i', 'u'],
            'u': ['a'],
             '': ['a', 'e', 'i', 'o', 'u']
        }

        visited = {}

        def dp(index, last):
            if index == n:
                return 1
            if (index, last) in visited:
                return visited[(index, last)]
            res = 0
            for char in transitions[last]:
                res += dp(index + 1, char)
            visited[(index, last)] = res % MOD
            return visited[(index, last)]
        return dp(0, '')
