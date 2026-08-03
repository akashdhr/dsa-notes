# Brute force
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        for i in range(len(s)):
            temp = s[:i] + s[i+1:]
            if temp == temp[::-1]:
                return True
        return False
    
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        arr = list(s)
        low = 0
        high = len(s) - 1
        while low <= high:
            if arr[low] == arr[high]:
                low += 1
                high -= 1
            else:
                return arr[low+1:high+1] == arr[low+1:high+1][::-1] or arr[low:high] == arr[low:high][::-1]
        return True


#time complexity: O(N) where N is the length of the string.
#space complexity: O(1) since we are using constant space to store the pointers and temporary variables.
        