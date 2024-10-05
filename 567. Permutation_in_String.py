class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1 = Counter(s1)
        for start in range(len(s2) - len(s1) + 1):
            count2 = defaultdict(int)
            for i in range(start, start + len(s1)):
                count2[s2[i]] += 1
            if count1 == count2:
                return True
        return False
