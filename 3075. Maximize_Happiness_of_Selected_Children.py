class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        dicrease=0
        sum_of_happy=0
        while k>0:
            curr_happy = happiness.pop()- dicrease
            sum_of_happy += curr_happy if curr_happy >=0 else 0
            dicrease+=1
            k-=1
        return sum_of_happy
