"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash={None:None}
        b=head
        while b:
            hash[b]=Node(b.val)
            b=b.next
        b=head
        while b:
            c=hash[b]
            c.next=hash[b.next]
            c.random=hash[b.random]
            b=b.next
        return hash[head]   