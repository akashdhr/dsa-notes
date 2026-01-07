class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        k_beauty = 0
        for i in range(len(num_str) - k + 1):
            num_temp = int(num_str[i:i+k])
            print(num_temp)
            if num_temp != 0 and num % num_temp == 0:
                k_beauty += 1
        return k_beauty

# Time complexity: O(N)
# Space complexity: O(1)