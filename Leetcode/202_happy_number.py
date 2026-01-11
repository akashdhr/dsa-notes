class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def find(num, curr_sum):
            if num == 1:
                return True
            if num in seen:
                return False
            seen.add(num)
            num_str = str(num)
            new_sum = 0
            for i in range(len(num_str)):
                new_sum += int(num_str[i]) * int(num_str[i])
            return find(new_sum, 0)
        return find(n, 0)
        