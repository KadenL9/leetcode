class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)

        pairs = []
        for x in range(len(nums)):
            left = x + 1
            right = len(nums) - 1

            while left < right:
                a = nums[x]
                b = nums[left]
                c = nums[right]
                total = a + b + c
                if total == 0:
                    pairs.append((a, b, c))
                    left += 1
                    right -= 1
                else:
                    if total < 0:
                        left += 1
                    else:
                        right -= 1
            
        return list(set(pairs))
