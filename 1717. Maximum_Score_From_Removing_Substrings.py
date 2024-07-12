class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def removing_substrings(s,sub1,sub2,score):
            points=0
            st=[]
            for ch in s:
                if(st and st[-1]==sub1 and sub2==ch):
                    st.pop()
                    points+=score
                else:
                    st.append(ch)
            return ''.join(st),points
        if(x>y):
            s,score1=removing_substrings(s,'a','b',x)
            s,score2=removing_substrings(s,'b','a',y)
        else:
            s,score1=removing_substrings(s,'b','a',y)
            s,score2=removing_substrings(s,'a','b',x)
        return score1+score2
