class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isChar(c):
            if ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9'):
                return True
            else:
                return False
        l = 0
        r = len(s) - 1
        while l <= r:
            while isChar(s[l]) == False and l < r:
                l += 1
            while isChar(s[r]) == False and l < r:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

# time complexity: O(N) where N is the length of the input string. We traverse the string once to check for alphanumeric characters and compare them, which takes O(N) time.
# space complexity: O(1) since we are using only a constant amount of extra space to store the left and right pointers and to perform character comparisons. We are not using any additional data structures that grow with the input size.