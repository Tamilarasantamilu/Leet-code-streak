class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        
        prefix = [0] 
        for i in range(len(nums)-1):
            prefix.append(prefix[-1] + (nums[i]%2 != nums[i+1]%2))
        
        def isSpecial(start, end):
            return (prefix[end] - prefix[start] == end - start)
           
        
        listbool = [isSpecial(query[0],query[1]) for query in queries]
        
        return listbool
                
            
        
