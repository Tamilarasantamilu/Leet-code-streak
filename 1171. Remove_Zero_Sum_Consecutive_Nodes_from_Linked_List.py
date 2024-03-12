class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        curr = head
        seen = set([0])
        total = 0
        while curr:
            nums.append(curr.val)
            total += curr.val
            if total in seen:
                curr_total = total
                total -= nums[-1]
                nums.pop()
                while total != curr_total:
                    seen.remove(total)
                    total -= nums[-1]
                    nums.pop()
            else: 
                seen.add(total)
            curr = curr.next
        dummy = ListNode()
        curr = dummy
        for num in nums:   
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next
