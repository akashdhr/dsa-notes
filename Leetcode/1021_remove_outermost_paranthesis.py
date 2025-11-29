# This is implemented using counters
# Same can be implemented with stack
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        cnt = 0
        for i in range(len(s)):
            # First encounter of ( 
            # Increase counter by 1. Do not add anything in res as this is outer para
            if s[i] == '(' and cnt == 0:
                cnt += 1
            # Count is greater than 1 so add this is in res and increment counter
            elif s[i] == '(' and cnt >= 1:
                res += s[i]
                cnt += 1
            # Count is greater than 1 so add in res and decrease counter as this is closing para. (>= is not used here because = condition will have outer para)
            elif s[i] == ')' and cnt > 1:
                res += s[i]
                cnt -= 1
            # Count is equal to 1 so no need to add to res as this is the outer closing bracket
            else:
                cnt -= 1
        return res
