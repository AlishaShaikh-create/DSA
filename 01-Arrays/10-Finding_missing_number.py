class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        sum_of_n = n*(n+1)//2
        result = 0
        for i in range(len(nums)):
            result += nums[i]  
        return sum_of_n - result   