class Solution:
    def convert(self, x: int, storage: list[int]) -> int:
        n: int = 0
        pieces: list[int] = []
        valid: bool = True
        while valid:
            acc: int = x % 10
            pieces.append(acc)
            x //= 10
            if x == 0: valid = False
        for piece in pieces[::-1]:
            n = n * 10 + storage[piece]
        return n

    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: self.convert(x, mapping))
        return nums
