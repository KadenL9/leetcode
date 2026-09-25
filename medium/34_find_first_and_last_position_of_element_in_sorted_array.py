class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        a = -1
        b = -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] != target:
                    a = mid
                    break
                else:
                    right = mid - 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        left = a + 1
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    b = mid
                    break
                else:
                    left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        if b == -1:
            return a, a
            
        return a, b
        