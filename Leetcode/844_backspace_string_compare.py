class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        str1 = []
        str2 = []
        for i in range(len(s)):
            if s[i] == '#':
                if str1:
                    str1.pop()
            else:
                str1.append(s[i])
        for i in range(len(t)):
            if t[i] == '#':
                if str2:
                    str2.pop()
            else:
                str2.append(t[i])
        str1 = ''.join(str1)
        print('str1: ', str1)
        str2 = ''.join(str2)
        print('str2: ', str2)
        return str1 == str2
            
        