# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if root == None:
                return 0,0

            l_s, l_n = solve(root.left)
            r_s, r_n = solve(root.right)
            n = l_n + r_n + 1 
            summ = l_s + r_s + root.val

            if (summ//n) == root.val:
                solve.ans += 1
            
            return summ , n
        
        solve.ans = 0
        solve(root)
        return solve.ans




