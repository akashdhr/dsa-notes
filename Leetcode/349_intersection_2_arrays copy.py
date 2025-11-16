class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a1 = set(nums1)
        a2 = set(nums2)
        common = []
        for i in a1:
            if i in a2:
                common.append(i)
        return common
        