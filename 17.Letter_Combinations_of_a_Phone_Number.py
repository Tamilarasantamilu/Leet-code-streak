class Solution:
    def __init__(self):
        self.lookup = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
    def letterCombinations(self, digits: str) -> List[str]:
        out = []
        for digit in digits:
            out = self.extendCombinations(out, self.lookup[digit])
        return out

    def extendCombinations(self, combinations: List[str], extension: List[str]) -> List[str]:
        if len(combinations) == 0:
            return extension
        out = []
        for combo in combinations:
            for letter in extension:
                out.append(combo+letter)
        return out