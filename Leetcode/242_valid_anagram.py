class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}
        for i in s:
            if i not in hashMap:
                hashMap[i] = 1
            else:
                hashMap[i] += 1
        
        for i in t:
            if i not in hashMap:
                return False
            else:
                hashMap[i] -= 1
        
        for v in hashMap.values():
            if v != 0:
                return False
        return True
        