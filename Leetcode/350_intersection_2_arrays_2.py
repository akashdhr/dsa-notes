class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = []
        l = r = 0

        while l < len(nums1) and r < len(nums2):
            if nums1[l] == nums2[r]:
                res.append(nums1[l])
                l += 1
                r += 1
            elif nums1[l] < nums2[r]:
                l += 1
            else:
                r += 1
        return res
        
# Follow up questions
# 1: If array is already sorted ignore the sort part
# 2: If nums1 is smaller use the below code
from collections import Counter

def intersect(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1  # ensure nums1 is smaller

    counts = Counter(nums1)
    res = []
    for num in nums2:
        if counts[num] > 0:
            res.append(num)
            counts[num] -= 1
    return res

        