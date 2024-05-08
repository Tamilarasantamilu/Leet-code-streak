class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        sortedScore = sorted(score,reverse = True)

        sortedAnswer = []

        sortedAnswer.insert(0,"Gold Medal")
        sortedAnswer.insert(1,"Silver Medal")
        sortedAnswer.insert(2,"Bronze Medal")

        for i in range(len(score)):
            if i > 2:
                sortedAnswer.append(str(i+1))
        
        
        answer = []
     
        for i in range(len(score)):
            answer.insert(score.index(score[i]),sortedAnswer[sortedScore.index(score[i])]) 


        return answer
