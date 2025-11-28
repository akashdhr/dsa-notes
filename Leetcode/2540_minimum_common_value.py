# Binary Search. TC: O(n1logn2)  
class Solution:
    def bSearch(self, nums, target):
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        for i in nums1:
            if self.bSearch(nums2, i):
                return i
        return -1

# Two Pointer approach. TC: O(n1 + n2)
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l1 = l2 = 0
        while l1 < len(nums1) and l2 < len(nums2):
            if nums1[l1] == nums2[l2]:
                return nums1[l1]
            elif nums1[l1] < nums2[l2]:
                l1 += 1
            else:
                l2 += 1
        return -1