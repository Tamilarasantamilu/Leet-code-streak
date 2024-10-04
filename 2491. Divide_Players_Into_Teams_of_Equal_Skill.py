class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left=0
        right=len(skill)-1
        sum_value=skill[left]+skill[right]
        result=0
        while left<=right:
            current_sum=skill[left]+skill[right]
            if current_sum!=sum_value:
                return -1
            result=result+(skill[left]*skill[right])
            left=left+1
            right=right-1
        return result
