class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        
        if d == 1:
            newRoot = TreeNode(v)
            newRoot.left = root
            return newRoot
        else:
            level_prev = list()
            # out = []
            level = [root]
            depth = 1
            while d != depth:
                # out.append([node.val for node in level])
                level_prev[:] = level
                level = [child for node in level_prev for child in (node.left, node.right) if child]
                depth += 1

            level_orig_with_none_nodes = [child for node in level_prev for child in (node.left, node.right)]

            for node in level_prev:
                node.left = TreeNode(v)
                node.right = TreeNode(v)
            
            
            new_level = [child for node in level_prev for child in (node.left, node.right) if child]
            
            
            if level:
                level_queue = deque(level_orig_with_none_nodes)
                
                for idx, node in enumerate(new_level):
                    if idx % 2 == 0:
                        if level_queue:
                            node.left = level_queue.popleft()
                    else:
                        if level_queue:
                            node.right = level_queue.popleft()

            return root
