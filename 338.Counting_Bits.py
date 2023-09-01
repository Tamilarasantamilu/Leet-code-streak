class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(x: int)-> int:
            count=0
            while x>0:
                bit_x = x & 1
                if bit_x == 1:
                    count+=1
                x >>= 1
            return count

        ans=[0]*(n+1)
        for x in range(n+1):
            ans[x]=count(x)

        return ans