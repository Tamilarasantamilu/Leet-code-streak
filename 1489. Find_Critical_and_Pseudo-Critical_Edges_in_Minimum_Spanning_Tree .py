class UnionFind:

    def __init__(self,n):
        self.parent = list(range(n))
        self.weights = 0

    def find(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x, y):
        self.parent[x] = y

    def mst(self,edges):
        for index, x, y, w in edges:
            rx, ry = self.find(x), self.find(y)
            if rx != ry:
                self.union(rx, ry)
                self.weights += w
        return self.weights



class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        sorted_edges = [[_i] + edge for _i, edge in enumerate(edges)]
        sorted_edges.sort(key=lambda x: x[-1])

        UF = UnionFind(n)
        weights = UF.mst(sorted_edges)

        key_edge = []
        not_key_edge = []
        for i, edge in enumerate(sorted_edges):

            _i, cx, cy, cw  = edge
            tmp_edges = sorted_edges[:i]+sorted_edges[i+1:]

            UF_select = UnionFind(n)
            UF_select.union(cx,cy)
            select_w = UF_select.mst(tmp_edges) + cw

            if select_w != weights: continue

            UF_remove = UnionFind(n)
            remove_w = UF_remove.mst(tmp_edges)

            if select_w != remove_w: key_edge.append(edge[0])
            else: not_key_edge.append(edge[0])

        return [key_edge, not_key_edge]