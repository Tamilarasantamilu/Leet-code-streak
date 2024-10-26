class Solution:
    def __init__(self):
        self.nodeToIndex = {}
        self.heightMap = []
        self.subtreeSize = []
        self.index = 0

    def treeQueries(self, root: TreeNode, queries: list[int]) -> list[int]:
        n = 100001
        self.heightMap = [0] * n
        self.subtreeSize = [0] * n
        self.dfs(root, 0)

        leftMax = [0] * self.index
        rightMax = [0] * self.index

        for i in range(self.index):
            leftMax[i] = self.heightMap[i]
            if i > 0:
                leftMax[i] = max(leftMax[i], leftMax[i - 1])

        for i in range(self.index - 1, -1, -1):
            rightMax[i] = self.heightMap[i]
            if i + 1 < self.index:
                rightMax[i] = max(rightMax[i], rightMax[i + 1])

        result = []
        for query in queries:
            nodeIndex = self.nodeToIndex[query]
            leftBound = nodeIndex
            rightBound = nodeIndex + self.subtreeSize[nodeIndex] - 1
            maxHeight = 0

            if leftBound > 0:
                maxHeight = max(maxHeight, leftMax[leftBound - 1])
            if rightBound + 1 < len(rightMax):
                maxHeight = max(maxHeight, rightMax[rightBound + 1])

            result.append(maxHeight)

        return result

    def dfs(self, root: TreeNode, height: int) -> int:
        if root is None:
            return 0
        
        self.nodeToIndex[root.val] = self.index
        self.heightMap[self.index] = height
        self.index += 1

        leftSize = self.dfs(root.left, height + 1)
        rightSize = self.dfs(root.right, height + 1)

        self.subtreeSize[self.nodeToIndex[root.val]] = 1 + leftSize + rightSize
        return 1 + leftSize + rightSize
