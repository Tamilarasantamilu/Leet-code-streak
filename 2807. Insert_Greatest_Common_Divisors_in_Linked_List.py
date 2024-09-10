class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        find=False
        prev=None
        while(curr.next):
            prev=curr
            curr=curr.next
            new=ListNode(math.gcd(prev.val,curr.val))
            prev.next=new
            new.next=curr
        return head
