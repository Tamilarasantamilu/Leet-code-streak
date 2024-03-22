def show_list(cur, N):
    print('-' * 50)
    for _ in range(N):
        print(cur.val)
        cur = cur.next
    print('-' * 50)


def get_2nd_half(cur, N):
    prev = None
    for _ in range(N // 2):
        prev, cur = cur, cur.next
    prev.next = None
    return cur

def reverse_list(cur, N):
    prev = None
    for _ in range(N):
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev

def isSame(head1, head2, N):
    for _ in range(N):
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next

    return True
    
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        N = 0
        cur = head
        for n in range(100000):
            if cur.next is None:
                N = n + 1
                break
            cur = cur.next

        if N == 1:
            return True

        head2 = get_2nd_half(head, N)
        if N % 2 == 1:
            head2 = head2.next
            N -= 1
        N //= 2
        head2 = reverse_list(head2, N)
        return isSame(head, head2, N)
