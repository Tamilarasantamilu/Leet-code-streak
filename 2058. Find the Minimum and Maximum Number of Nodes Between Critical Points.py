# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        li    = [] 
        point = []

        while head is not None :
            li.append(head.val)
            head = head.next

        mi = int(10e5)
        j = 0
        for i in range(1,len(li)-1): 
            if (li[i] > li[i-1] and li[i] > li[i+1]) or (li[i] < li[i-1] and li[i] < li[i+1]) :
                point.append(i+1) 
                if j >0 : mi = min(mi, point[j]-point[j-1] )
                j += 1
        if len(point) < 2  :
            return [-1,-1]
        else:
            return [ mi , (point[len(point)-1] - point[0]) ]    
