# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self, maxD = 0):
        # the value to store the current max diameter
        self.maxD = maxD

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # the recursive function to be called recursively
        # on the current node
        def checkRecur(node):
            if (not node):
                return 0
            # get the depth of left & right child tree
            leftDepth = checkRecur(node.left)
            rightDepth = checkRecur(node.right)
            # update the max Diameter
            if (self.maxD < leftDepth + rightDepth):
                self.maxD = leftDepth + rightDepth
            # return the maxDepth
            if (leftDepth < rightDepth):
                return 1 + rightDepth
            return 1 + leftDepth

        if (not root):
            return 0
        # start from the root node
        checkRecur(root)
        return self.maxD