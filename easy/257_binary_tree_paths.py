class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        def getPaths(root, currPath):
            if root == None:
                return
            if root.left == None and root.right == None:
                paths.append(currPath + [root.val])

            getPaths(root.left, currPath + [root.val])
            getPaths(root.right, currPath + [root.val])

    
        paths = []
        getPaths(root, [])

        format_paths = []
        for path in paths:
            currpath = str(path[0])
            for x in range(1, len(path)):
                currpath += "->" + str(path[x])
            format_paths.append(currpath)

        return format_paths