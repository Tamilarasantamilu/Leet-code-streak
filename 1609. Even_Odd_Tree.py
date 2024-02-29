# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        bfs = deque()
        bfs.append((root, 0))
        while bfs:
            node, level = bfs.popleft()
            if node.val % 2 == level % 2:
                return False
            if bfs and bfs[0][1] == level:
                if level % 2 == 1 and bfs[0][0].val >= node.val:
                    return False
                if level % 2 == 0 and bfs[0][0].val <= node.val:
                    return False
            if node.left:
                bfs.append((node.left, level + 1))
            if node.right:
                bfs.append((node.right, level + 1))
        return True
