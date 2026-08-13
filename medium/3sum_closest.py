class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums = sorted(nums)
        
        closest = nums[0] + nums[1] + nums[2]

        for x in range(len(nums)):
            left = x + 1
            right = len(nums) - 1

            while left < right:
                total = nums[x] + nums[left] + nums[right]

                if total == target:
                    return total

                if abs(target - total) < abs(target - closest):
                    closest = total
                            
                if target - total > 0:
                    left += 1
                else:
                    right -= 1
            
        return closest