class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ans = [0] * (m + n)
        l1 = l2 = 0
        k = 0
        while l1 < m and l2 < n:
            if nums1[l1] <= nums2[l2]:
                ans[k] = nums1[l1]
                k += 1
                l1 += 1
            else:
                ans[k] = nums2[l2]
                k += 1
                l2 += 1
        while l1 < m:
            ans[k] = nums1[l1]
            l1 += 1
            k += 1
        while l2 < n:
            ans[k] = nums2[l2]
            l2 += 1
            k += 1
        for l in range(m + n):
            nums1[l] = ans[l]
        



# time complexity: O(m + n) where m and n are the lengths of the input arrays nums1 and nums2 respectively. We traverse both arrays once to merge them.
# space complexity: O(1) since we are modifying nums1 in-place and not using any additional data structures that grow with the input size.