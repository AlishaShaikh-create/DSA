class Solution:
    def rotateArrayByOne(self, nums):
        for i in range(1,len(nums)):
            nums[i]  , nums[i-1] = nums[i-1] , nums[i]
        return  nums 