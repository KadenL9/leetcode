class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if left == mid:
                break

            if nums[left] < nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[left] <= target or nums[mid] >= target:
                    right = mid
                else:
                    left = mid
                    
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1