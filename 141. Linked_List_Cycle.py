class Solution(object):
    def hasCycle(self, head):

        visited = set()
        current = head
        
        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next
            
        return False
      
