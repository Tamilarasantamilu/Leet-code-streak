class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        nodes = set(leftChild + rightChild)

        root = -1 
        if -1 in nodes:
            nodes.remove(-1)
        for i in range(n + 1):
            if i not in nodes:
                root = i
                break

        if root == -1 or len(nodes) != n - 1:
            return False

        nodes = set()

        def dfs(index):
            if index == -1:
                return True
            l, r = leftChild[index], rightChild[index]
            if l in nodes or r in nodes:
                return False
            if l != -1:
                nodes.add(l)
            if r != -1:
                nodes.add(r)
            return dfs(l) and dfs(r)
        return dfs(root) and len(nodes) == n - 1
