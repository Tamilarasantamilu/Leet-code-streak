# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def ispalindromic(counts):
            odd_count = 0
            for count in counts.values():
                if count % 2 != 0:
                    odd_count += 1
                if odd_count > 1:
                    return False
            return True

        def dfs(node, counts):
            if not node:
                return 0
                
            counts[node.val] += 1
            # If it's a leaf node, check if the path is suedo-palindromic
            if not node.left and not node.right:
                if ispalindromic(counts):
                    counts[node.val] -= 1 # Backtrack(return and choose new path(node) again.)
                    return 1
                else:
                    counts[node.val] -= 1 # Backtrack(return and choose new path(node) again.)
                    return 0

            # Recursivly traverse left and right subtrees
            left_count = dfs(node.left, counts)
            right_count = dfs(node.right, counts)

            counts[node.val] -= 1 # Backtrack(return and choose new path(node) again.)

            return left_count + right_count

        # Start DFS from the root with an empty counts dictonary
        return dfs(root, defaultdict(int))
