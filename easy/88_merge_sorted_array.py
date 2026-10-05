class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m_idx = m - 1
        n_idx = n - 1
        idx = m + n - 1
        while idx >= 0:
            print(m_idx, n_idx, idx)
            if m_idx < 0:
                nums1[idx] = nums2[n_idx]
                n_idx -= 1
            elif n_idx < 0:
                nums1[idx] = nums1[m_idx]
                m_idx -= 1
            elif nums1[m_idx] > nums2[n_idx]:
                nums1[idx] = nums1[m_idx]
                m_idx -= 1
            else:
                nums1[idx] = nums2[n_idx]
                n_idx -= 1
            
            idx -= 1
        
