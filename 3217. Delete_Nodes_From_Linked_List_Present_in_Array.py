# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        nums = set(nums)

        cur = head
        dummy = ListNode(0)
        temp = dummy


        while cur:
            if cur.val in nums:
                cur = cur.next
            
            else:
                dummy.next = cur
                dummy = dummy.next
                t = cur.next
                cur.next = None
                cur = t
        
        return temp.next
            
        
