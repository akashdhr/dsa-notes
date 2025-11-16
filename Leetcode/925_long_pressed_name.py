class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        np = 0 #pointer for tracking name
        tp = 0 #pointer for tracking typed
        if len(name) > len(typed):
            return False
        while tp < len(typed):
            # if both values are same just increase the pointers
            if np < len(name) and name[np] == typed[tp]:
                np += 1
                tp += 1
            # if the values are not same, check if typed value is matching previous index of name
            elif tp > 0 and typed[tp] == typed[tp-1]:
                tp += 1
            else:
                return False
        return np == len(name)