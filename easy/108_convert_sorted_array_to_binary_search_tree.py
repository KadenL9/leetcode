# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        return self.convertToBST(nums)
        
    def convertToBST(self, nums):
        if nums == []:
            return None
            
        middle = len(nums) // 2
        root = TreeNode(nums[middle], None, None)

        root.left = self.convertToBST(nums[0: middle])
        root.right = self.convertToBST(nums[middle + 1:])

        return root