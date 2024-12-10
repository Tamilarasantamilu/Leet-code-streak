from collections import defaultdict
class Solution:
    def maximumLength(self, s: str) -> int:
        str_idx_map = defaultdict(list)

        for i, t in enumerate(s):
            str_idx_map[t].append(i)

        ans = [-1]
        for t in str_idx_map:
            indexes = str_idx_map[t]
            if len(indexes) >=3:
                self.dfs(indexes, 1, set(indexes), ans)

        return ans[0] 

    def dfs(self, end_indexes, length, index_set, ans):
        ans[0] = max(ans[0], length)

        next_indexes = []
        for idx in end_indexes:
            if idx+1 in index_set:
                next_indexes.append(idx+1)

        if len(next_indexes) >= 3:
            self.dfs(next_indexes, length+1, index_set, ans)
