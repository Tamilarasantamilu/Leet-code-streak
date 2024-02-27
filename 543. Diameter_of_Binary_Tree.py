class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0
        def dfs(node):
            if not node: 
                return 0
            nonlocal res
            l,r=dfs(node.left), dfs(node.right)
            res=max(res,l+r)
            return max(l,r)+1
        dfs(root)
        return res
