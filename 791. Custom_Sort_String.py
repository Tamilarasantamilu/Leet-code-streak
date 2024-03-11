class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order = order[::-1]
        c = []
        for i in order:
            if i in s:
                c.insert(0, i * s.count(i))
        for j in s:
            if j not in order:
                c.append(j)
        return ''.join(c)
