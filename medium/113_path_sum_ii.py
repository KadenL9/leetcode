class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        if root == None:
            return []
        
        if root.left == None and root.right == None:
            if root.val == targetSum:
                return [[root.val]]
        
        left = self.pathSum(root.left, targetSum - root.val)
        right = self.pathSum(root.right, targetSum - root.val)

        currPaths = left + right
        newPaths = []
        for path in currPaths:
            if path != []:
                newPaths.append([root.val] + path)
        
        return newPaths
        