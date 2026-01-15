class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        low = 0
        high = n - 1
        start = n
        res = []
        while low <= high:
            mid = (low+high)//2
            if x <= arr[mid]:
                start = mid
                high = mid - 1
            else:
                low = mid + 1
        left = start - 1
        right = start
        while k > 0:
            if left < 0:
                res.append(arr[right])
                right += 1
            elif right >= n:
                res.append(arr[left])
                left -= 1
            elif abs(arr[left] - x) <= abs(x - arr[right]):
                res.append(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1
            k -= 1
        return sorted(res)

        
# time complexity: O(log N + K log K) where N is the number of elements in arr. O(log N) for binary search and O(K log K) for sorting the result.
# space complexity: O(K) for storing the result.