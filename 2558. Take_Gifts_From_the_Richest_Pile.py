import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
             m=max(gifts)
             val=(math.floor(pow(m,0.5)))
             gifts.remove(m)
             gifts.append(val)
        return sum(gifts)
