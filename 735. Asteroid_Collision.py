class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for i,e in enumerate(asteroids):
            flag = False
            if e<0:                                                    
                for j in range(len(s)):                                
                    if s[-1]<0: s.append(e); flag = True; break         
                    else:                                               
                        if s[-1]>abs(e): flag = True; break            
                        elif s[-1]<abs(e): s.pop()                      
                        else: s.pop(); flag = True; break               
                if flag!=True: s.append(e)                              
            else:                                                       
                s.append(e)
        return s