class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller_head = ListNode(0)
        greater_head = ListNode(0)
        smaller = smaller_head
        greater = greater_head
        while head:
            if head.val < x:
                smaller.next = head
                smaller = smaller.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next
        smaller.next = greater_head.next
        greater.next = None
        
        return smaller_head.next