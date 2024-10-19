class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def reverseAndInvert(temp):
            latestString = temp[-1]
            latestString = [i for i in latestString]
            for i in range(len(latestString)):
                if latestString[i] == '0':
                    latestString[i] = '1'
                else:
                    latestString[i] = '0'
            
            res = '1' + ''.join(latestString[::-1])
            return res

        si = '0'
        temp = []
        temp.append(si)
        for i in range(n - 1):
            si += reverseAndInvert(temp)
            temp.append(si)
        return temp[-1][k-1]
