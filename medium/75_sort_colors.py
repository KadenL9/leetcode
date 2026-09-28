class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1
        x = 0

        while x < len(nums):
            print(nums)
            if nums[x] == 0 and x > l:
                nums[x], nums[l] = nums[l], nums[x]
                l += 1
            elif nums[x] == 2 and x < r:
                nums[x], nums[r] = nums[r], nums[x]
                r -= 1
            else:
                x += 1