# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

        M = mountain_arr.length()
        l, r = 1, M - 2
        visited = {}

        def get_val(idx):
            if idx in visited:
                return visited[idx]
            val = mountain_arr.get(idx)
            visited[idx] = val
            return val
        
        while l <=r:
            p = (l + r) // 2
            val = get_val(p)
            left = get_val(p - 1)
            if left < val:
                right = get_val(p + 1)
                if val > right:
                    res = p
                    if val == target:
                        return res
                    break
                else:
                    l = p + 1
            else:
                r = p - 1
       
        def search(l, r, ascending):
            while l <= r:
                p = (l + r) // 2
                val = get_val(p)
                if val == target:
                    return p
                if val < target:
                    if ascending:
                        l = p + 1
                    else:
                        r = p - 1
                else:
                    if ascending:
                        r = p - 1
                    else:
                        l = p + 1
            return -1  
        climb = search(0, res - 1, True)
        if climb != -1:
            return climb
        
        return search(res + 1, M - 1, False)        
