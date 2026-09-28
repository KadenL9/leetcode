class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return

        right = root.right
        root.right = root.left
        root.left = None

        self.flatten(root.right)

        while root.right != None:
            root = root.right

        root.right = right

        self.flatten(root.right)

