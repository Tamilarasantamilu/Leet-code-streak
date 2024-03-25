from collections import Counter
from typing import List

class Solution:
    def findDuplicates(self, num: List[int]) -> List[int]:
        cnt = Counter(num)
        duplicates = []
        for key, val in cnt.items():
            if val == 2:
                duplicates.append(key)
        return duplicates
