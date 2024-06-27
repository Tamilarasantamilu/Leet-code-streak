class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first = edges[0]

        node = None

        if edges[1][0] in first:
            node = edges[1][0]
        else:
            node = edges[1][1]
        
        return node
        
