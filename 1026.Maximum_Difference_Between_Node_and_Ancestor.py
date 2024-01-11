# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if root == None:
            return [0, 100000, 0] # max, min, result of diff
        if root.left == None and root.right == None: # leaf node
            return [root.val, root.val, 0]

        l1 = self.solve(root.left)
        l2 = self.solve(root.right)

        a = max(l1[0], l2[0]) # a -> max from subtrees
        b = min(l1[1], l2[1]) # b -> min from subtrees
        c = max(abs(root.val - a), abs(root.val - b)) # c -> max differnce
        return [max(a, root.val), min(b, root.val), max(l1[2], l2[2], c)]
        # new -> max value, min value, max difference 
        
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = self.solve(root)
        return res[2]
