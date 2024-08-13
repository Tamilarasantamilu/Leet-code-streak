class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:
                result.append(path)
                return
            
            if target < 0:
                return 
            
            for i in range(start, len(candidates)):
                # skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # include the current number and move to the next
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])
            
        candidates.sort()
        result = []
        backtrack(0, target, [])
        return result 
