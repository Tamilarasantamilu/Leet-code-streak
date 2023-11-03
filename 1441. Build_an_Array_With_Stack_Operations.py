class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        if not target:
            return []
        res = []
        for i in range(1,n+1):
            if i in target:
                res.append('Push')
            elif i not in target and i<=target[-1]:
                res.append("Push")
                res.append("Pop")
            if i==target[-1]:
                break
        return res
