# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findMode(self, root: [TreeNode]) -> list[int]:  
        occurences = {} 
        def search(node):
                if node != None:
                    search(node.left)
                    occurences[node.val] = occurences.get(node.val, 0) + 1
                    search(node.right)
        
        search(root)
        modes = []
        max_count = max(occurences.values())
        for key in occurences:
            if occurences[key] == max_count:
                modes.append(key)

        return(modes)
