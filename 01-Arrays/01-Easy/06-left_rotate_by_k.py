class Solution:
    def rotateArray(self, nums, k: int) -> None:
        k = k % len(nums)
        while k :
            for i in range(1 ,len(nums)):
                temp = nums[i-1]
                nums[i-1] = nums[i]
                nums[i] = temp
            k-=1    
        return nums