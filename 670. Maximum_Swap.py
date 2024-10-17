class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(map(int, str(num)))  
        swap = 1
        i = 0
        j = len(num) - 1
        
        while swap:
            while i < len(num) - 1 and num[i] == max(num[i:]):
                i += 1
            while j > 0 and num[j] < max(num[i:]):
                j -= 1
            if i < j: 
                num[i], num[j] = num[j], num[i]
                swap = 0 
            else:
                swap = 0  
        
        return int(''.join(map(str,num)))
