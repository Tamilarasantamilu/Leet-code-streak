
class Solution:
    
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
      
        def dfs(head: Optional[ListNode], node: Optional[TreeNode]) -> bool:
            if not head: 
                return True
            if not node:  
                return False
            if head.val != node.val:  
                return False
   
            return dfs(head.next, node.left) or dfs(head.next, node.right)
        

        if not root:
            return False
  
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
