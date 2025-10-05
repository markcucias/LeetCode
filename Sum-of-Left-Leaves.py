# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isLeaf(root: Optional[TreeNode]) -> bool:
        if root.left == None and root.right == None:
            return True
        return False



class Solution:

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = 0
        if isLeaf(root):
            return result

        # Adding up the reaf to the result
        if root.left != None and isLeaf(root.left):
            result += root.left.val

        # Checking leafs on the left
        if root.left != None:
            result += self.sumOfLeftLeaves(root.left)

        # Checking leafs on the right
        if root.right != None:
            result += self.sumOfLeftLeaves(root.right)

        

        return result
        
        
    

    