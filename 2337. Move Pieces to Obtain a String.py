class Solution:
    def canChange(self, a: str, b: str) -> bool:
        n = len(a)
        i, j = 0, 0
        if(a.count('L') != b.count('L') or a.count('R') != b.count('R')):
            return False
        while(i < n and j < n):
            if(a[i] == '_'):
                i += 1
            elif(b[j] == '_'):
                j += 1
            elif(a[i] == b[j] and a[i] == 'L' and i>=j):
                i += 1
                j += 1
            elif(a[i] == b[j] and a[i] == 'R' and i<=j):
                i += 1
                j += 1
            else:
                return False
        return True

        
