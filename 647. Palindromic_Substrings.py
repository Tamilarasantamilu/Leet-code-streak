class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        
        if n == 0:
            return 0

        for i in range(n): #1
            count += 1 #2
            right = i + 1 #3
            left = i - 1 #4
            
            while right < n and s[right] == s[i]: #5
                right+=1
                count+=1
                
            while right < n and left >= 0 and s[left] == s[right]: #6
                count += 1
                left -= 1
                right += 1
            
        return count
