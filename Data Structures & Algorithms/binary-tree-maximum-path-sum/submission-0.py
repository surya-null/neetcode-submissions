# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res =[root.val]
        def dfs(node):

            if not node:
                return 0
            
            leftMax = max(dfs(node.left),0)
            rightMax =max(dfs(node.right),0)

            # split and check res

            res[0]= max(node.val+leftMax+rightMax,res[0])

            #return value without split: we have to choose between left or right 

            return node.val+max(leftMax,rightMax)

        dfs(root)   
        return res[0]

