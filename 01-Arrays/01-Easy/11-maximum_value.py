class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        value = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count +=1
                value = max(count , value)
            else :
                count = 0
        return value    