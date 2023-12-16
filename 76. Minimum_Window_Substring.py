
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ideal_window = {}
        for c in t:
            if c not in ideal_window:
                ideal_window[c] = 1
            else:
                ideal_window[c]+=1
        curr_window = {}
        bad_char = set(ideal_window.keys())
        for i,c in enumerate(s):
            if c in ideal_window:
                if c not in curr_window:
                    curr_window[c] = 1
                else:
                    curr_window[c] += 1
                if c in bad_char and curr_window[c] >= ideal_window[c]:
                    bad_char.remove(c)
                if len(bad_char) == 0:
                    break
        else:
            return ""
        # so we found the ideal substring starting from 0
        # s[:(i+1)]
        # a smaller string would always be less than this one, if it exists
        pointer1,pointer2 = 0,i+1
        best1,best2 = pointer1,pointer2
        while pointer1 < len(s) and pointer2 <= len(s):
            # first try to shrink left
            while len(bad_char) == 0:
                best1,best2 = pointer1,pointer2
                if s[pointer1] in ideal_window:
                    curr_window[s[pointer1]] -= 1
                    if curr_window[s[pointer1]] < ideal_window[s[pointer1]]:
                        bad_char.add(s[pointer1])
                pointer1 += 1
            # now try to advance (the entire window) 1 to the right to see if it fixes it
            if pointer2 == len(s):
                break
            else:
                c = s[pointer2]
                if c in ideal_window:
                    curr_window[c]+=1
                    if c in bad_char and curr_window[c] >= ideal_window[c]:
                        bad_char.remove(c)
                c = s[pointer1]
                if c in ideal_window:
                    curr_window[c]-=1
                    if curr_window[c] < ideal_window[c]:
                        bad_char.add(c)
                pointer2+=1
                pointer1+=1
        return s[best1:best2]
        
