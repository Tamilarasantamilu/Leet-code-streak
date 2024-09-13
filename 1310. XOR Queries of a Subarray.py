class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        record = [*accumulate(arr, operator.xor, initial=0)]
        for st, ed in queries:
            yield record[st]^record[ed+1]
