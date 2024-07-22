class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        result=[]
        for n,h in zip(names,heights):
            result.append([n,h])
        sorted_result=sorted(result,key=lambda x:x[1],reverse=True)
        
        final_result=[]
        for i in sorted_result:
            res=i[0]
            final_result.append(res)
        return(final_result)
