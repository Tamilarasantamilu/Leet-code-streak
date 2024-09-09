class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        left, right, top, bottom = 0, n, 0, m

        while head:
            row = top
            for col in range(left, right):
                matrix[row][col] = head.val
                if not head.next:
                    return matrix
                head = head.next
            col = right - 1
            for row in range(top + 1, bottom):
                matrix[row][col] = head.val
                if not head.next:
                    return matrix
                head = head.next

            row = bottom - 1
            for col in range(right - 2, left - 1, -1):
                matrix[row][col] = head.val
                if not head.next:
                    return matrix
                head = head.next

            col = left
            for row in range(bottom - 2, top, -1):
                matrix[row][col] = head.val
                if not head.next:
                    return matrix
                head = head.next

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return matrix
