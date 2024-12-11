class Solution:
	def maximumBeauty(self, nums: List[int], k: int) -> int:

		result = 0

		hash_map = defaultdict(int)

		for num in nums:
			hash_map[num - k] = hash_map[num - k] + 1
			hash_map[num + k + 1] = hash_map[num + k + 1] - 1

		keys = sorted(list(hash_map.keys()))

		current_max = 0

		for key in keys:

			current_max = current_max + hash_map[key]

			result = max(result , current_max)

		return result
		
