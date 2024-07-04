# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
  def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # Initialize a dummy node to form the new list
    dummy = ListNode(0)
    current = dummy
    
    # Skip the initial zero
    head = head.next
    
    # Initialize sum variable
    total = 0
    
    while head:
      if head.val == 0:
        # If zero is encountered, create a new node with the sum
        current.next = ListNode(total)
        current = current.next
        # Reset the sum for the next segment
        total = 0
      else:
        # Accumulate the sum between zeros
        total += head.val
      head = head.next
    
    return dummy.next
