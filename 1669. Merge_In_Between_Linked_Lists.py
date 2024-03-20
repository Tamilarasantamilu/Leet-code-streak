class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        r1, r2 = None, None
        curr = list1
        counter = 0 
        while curr:
            if counter+1 == a:
                r1 = curr
            if counter == b:
                r2 = curr.next
                break
            curr = curr.next
            counter += 1
        r1.next = list2
        while r1.next:
            r1 = r1.next
        r1.next = r2
        return list1
        
