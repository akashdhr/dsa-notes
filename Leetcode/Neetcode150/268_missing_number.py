class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        #Storing the respective indices presence in the frequency array
        freqArr = [0] * (max(nums)+2) 
        #print(freqArr)
        res = 0
        for i in nums:
            freqArr[i] = 1
        #print(freqArr)
        for j in range(len(freqArr)):
            if freqArr[j] == 0:
                res = j
                break
        return res
        