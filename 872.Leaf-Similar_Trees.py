# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        x,y=[],[]
        def preorder(root,l):
            if root:
                if not root.left and not root.right:
                    l.append(root.val)
                preorder(root.left,l);preorder(root.right,l)
            else:return
        preorder(root1,x);preorder(root2,y)
        if x==y:return True
        else:return False
