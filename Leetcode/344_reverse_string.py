class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        low = 0
        high = len(s) - 1

        while low <= high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1
        
        return s

# time complexity: O(N) where N is the length of the string.
# space complexity: O(1) since we are using constant space to store the pointers and temporary variables.
        