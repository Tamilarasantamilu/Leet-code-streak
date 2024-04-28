class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        result = [0] * n
        count = [1] * n
        tree = collections.defaultdict(set)

        for i,j in edges:
            tree[i].add(j)
            tree[j].add(i)
        
        def postOrder(node, parent=None):
            for child in tree[node]:
                if child == parent:
                    continue
                postOrder(child,node)
                count[node]+=count[child]
                result[node]+=result[child] + count[child]
        
        def preorder(node, parent=None):
            for child in tree[node]:
                if child == parent:
                    continue
                result[child] = result[node] - count[child] + (n - count[child])
                preorder(child,node)
        
        postOrder(0)
        preorder(0)
        return result
