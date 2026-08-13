class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums = sorted(nums)

        pairs = []
        for x in range(len(nums)):
            for y in range(x + 1, len(nums)):
                left = y + 1
                right = len(nums) - 1

                while left < right:
                    a = nums[x]
                    b = nums[y]
                    c = nums[left]
                    d = nums[right]
                    total = a + b + c + d
                    if total == target:
                        pairs.append((a, b, c, d))
                        left += 1
                        right -= 1
                    else:
                        if total < target:
                            left += 1
                        else:
                            right -= 1
            
        return list(set(pairs))