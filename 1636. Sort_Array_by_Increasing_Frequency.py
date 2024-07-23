class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        def updateCounts(dic, a):
            if a in dic: dic[a] += 1
            else: dic[a] = 1
            return dic
        counts = reduce(updateCounts, nums, {})
        counts_sort = dict(sorted(counts.items(), key=lambda a: (a[1], -a[0])))
        nest = ( [value] * count for (value, count) in counts_sort.items() )
        return [ a for sublist in nest for a in sublist ]
