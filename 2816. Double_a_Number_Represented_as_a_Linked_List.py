# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        def reverse(head):
            curr=head
            prev=None
            while curr!=None:
                front=curr.next
                curr.next=prev
                prev=curr
                curr=front
            return prev
        temp=reverse(head)
        carry=0
        self.head2=None
        self.temp2=None
        while temp!=None:
            summ=temp.val * 2 +carry
            newNode=ListNode(summ%10)
            carry=summ//10
            if self.head2==None:
                self.head2=newNode
                self.temp2=self.head2
            else:
                self.temp2.next=newNode
                self.temp2=newNode
            temp=temp.next
        if carry!=0:
            newNode=ListNode(carry)
            self.temp2.next=newNode
            self.temp2=newNode
            return reverse(self.head2)
        else:
            return reverse(self.head2)
