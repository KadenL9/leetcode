class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def getNums(root, currVal):
            if root == None:
                return
            elif root.left == None and root.right == None:
                nums.append(currVal * 10 + root.val)
            else:
                getNums(root.left, currVal * 10 + root.val)
                getNums(root.right, currVal * 10 + root.val)

        nums = []
        getNums(root, 0)

        return sum(nums)
