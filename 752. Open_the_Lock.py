class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        q = deque([(0,'0000')])

        def getChildren(lock):
            res = []
            for i in range(4):
                lock1 = lock[:i]+str((int(lock[i])+1)%10)+lock[i+1:]
                lock2 = lock[:i]+str((int(lock[i])-1+10)%10)+lock[i+1:]
                res+=[lock1,lock2]
            return res

        while q:
            turns,code = q.popleft()
            if code==target:
                return turns

            if code in visited:
                continue

            visited.add(code)

            for child in getChildren(code):
                if child not in visited:
                    q.append((turns+1,child))

        return -1
