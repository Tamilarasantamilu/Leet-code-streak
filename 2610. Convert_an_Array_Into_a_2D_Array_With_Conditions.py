class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
            if len(res) < counts[num]:
                res.append([])
            res[counts[num] - 1].append(num)
        return res
