class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start, used_substrings):
            if start == len(s):
                return len(used_substrings)

            max_splits = 0
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if substring not in used_substrings:
                    used_substrings.add(substring)
                    max_splits = max(max_splits, backtrack(end, used_substrings))
                    used_substrings.remove(substring)
            return max_splits

        return backtrack(0, set())
