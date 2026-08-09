# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = (low+high)//2
            curr = guess(mid)
            if curr == -1:
                high = mid - 1
            elif curr == 1:
                low = mid + 1
            else:
                return mid

# time complexity: O(logN) where N is the range of numbers from 1 to n.
# space complexity: O(1) as we are using constant space.