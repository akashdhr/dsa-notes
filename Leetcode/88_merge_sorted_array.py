class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1 #last index of nums1 (excluding the blank values)
        j = n - 1 #last index of nums2
        k = m + n -1 #last index of final nums1

        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
            else:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1

        #in case all nums1 exhausted and nums2 still pending
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

        print(nums1)

# time complexity: O(m + n) where m and n are the lengths of the input arrays nums1 and nums2 respectively. We traverse both arrays once to merge them.
# space complexity: O(1) since we are modifying nums1 in-place and not using any additional data structures that grow with the input size.