# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        char_arr = list(s)
        cnt = 0
        for i in range(len(s) - 3 + 1):
            temp = s[i:i+3]
            if len(set(temp)) == 3:
                cnt += 1
        return cnt


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0

        cnt = 0
        freq = {}

        # initialize first window
        for c in s[:3]:
            freq[c] = freq.get(c, 0) + 1
        if len(freq) == 3:
            cnt += 1

        for i in range(3, len(s)):
            # remove outgoing char
            out = s[i - 3]
            freq[out] -= 1
            if freq[out] == 0:
                del freq[out]

            # add new char
            in_c = s[i]
            freq[in_c] = freq.get(in_c, 0) + 1

            if len(freq) == 3:
                cnt += 1

        return cnt