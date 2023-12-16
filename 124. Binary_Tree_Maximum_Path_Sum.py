class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self._maxPathSum = -pow(2, 31) - 1
        self.findMaxPathSum(root)
        return self._maxPathSum

    def findMaxPathSum(self, node):
        if node is None:
            return 0
        
        leftTreeSum = self.findMaxPathSum(node.left)
        rightTreeSum = self.findMaxPathSum(node.right)
        
        treeSum = max(max(leftTreeSum, rightTreeSum) + node.val, node.val)
        subtreeSum = leftTreeSum + rightTreeSum + node.val
        
        pathSum = max(treeSum, subtreeSum)
        self._maxPathSum = max(self._maxPathSum, pathSum)
        
        return treeSum
