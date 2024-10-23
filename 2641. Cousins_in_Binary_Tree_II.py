class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        queue = deque([(root, None)])
        
        while queue:
            level_size = len(queue)
            parent_to_sum = defaultdict(int)
            total_sum = 0

            nodes_at_level = []
            for _ in range(level_size):
                node, parent = queue.popleft()
                nodes_at_level.append((node, parent))
                total_sum += node.val
                parent_to_sum[parent] += node.val
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))

            for node, parent in nodes_at_level:
                node.val = total_sum - parent_to_sum[parent]

        return root
