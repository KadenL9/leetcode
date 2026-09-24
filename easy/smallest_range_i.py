class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        maxnum = max(nums)
        minnum = min(nums)

        if abs(maxnum - minnum) <= k * 2:
            return 0
        
        return maxnum - k - (minnum + k)