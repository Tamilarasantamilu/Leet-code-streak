class Solution:
    def hammingWeight(self, n: int) -> int:
        res =0
        while n:
            #you can use both approaches
            #res +=n%2
            #n = n>>1
            n&=n-1
            res+=1
        return res
