class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count_dict = Counter(arr)
        distinct_items = [item for item in arr if count_dict[item] == 1]
        if len(distinct_items) >= k:
            return distinct_items[k-1]
        else:
            return ""
