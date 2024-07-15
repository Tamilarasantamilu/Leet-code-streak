# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:

        mp=dict()
        root=TreeNode(descriptions[0][0])
        mp[descriptions[0][0]]=[root,-1]

        for data in descriptions:
            
            nd=None

            # if the node has come for th first tim then make it and 
            # add it to the map
            if(data[0] not in mp):

                nd=TreeNode(data[0])

                # here -1 means it has no parent so it can be main
                # root
                mp[data[0]]=[nd,-1]
            
            else:

                nd=mp[data[0]][0]
                
            
            # same for child also 
            child=None
            if(data[1]  not in mp):
                
                child=TreeNode(data[1]) 

                # update the parent of child as the nd 
                mp[data[1]]=[child,nd]

            else:

                child=mp[data[1]][0]

                # in this case as the child has already there in mp
                # so it mean earlier it is parent of some node 
                # and now as this is the child of nd so make
                # its parent as nd 
                mp[data[1]][1]=nd
                
                

            # now check whether it is the left or the right child of the node
            if(data[2]==1):

                nd.left=child

            else:

                nd.right=child 

       
        # as the main root has nno parent so it
        # mean the root with -1 parnet is the main root ...
        for key in mp:

            if(mp[key][1]==-1):

                root=mp[key][0]


        return root
