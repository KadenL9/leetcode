class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for x in range(len(nums)):
            diff = target - nums[x]
            if diff in indices:
                return [indices[diff], x]
            
            indices[nums[x]] = x
        
        return []