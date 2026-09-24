class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        x = 0
        y = 0
        while x < len(nums1) or y < len(nums2):
            if x >= len(nums1):
                merged.append(nums2[y])
                y += 1
            elif y >= len(nums2):
                merged.append(nums1[x])
                x += 1
            elif nums1[x] <= nums2[y]:
                merged.append(nums1[x])
                x += 1
            else:
                merged.append(nums2[y])
                y += 1
        
        total = len(nums1) + len(nums2)
        if len(merged) % 2 == 0:
            return (merged[total // 2 - 1] + merged[total // 2]) / 2
        else:
            return merged[total // 2]
