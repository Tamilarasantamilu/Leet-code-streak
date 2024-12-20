# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        frontier = deque()
        frontier.appendleft(root)
        level = 0
        while frontier:
            record = []
            for i in range(len(frontier)):
                curr_node = frontier.pop()
                if level & 1:
                    record.append(curr_node)
                if curr_node.left:
                    frontier.appendleft(curr_node.left)
                if curr_node.right:
                    frontier.appendleft(curr_node.right)
            level += 1
            if record:
                p = 0
                mid = len(record)//2
                while p < mid:
                    record[p].val, record[len(record)-p-1].val = record[len(record)-p-1].val, record[p].val
                    p += 1
        return root
                
