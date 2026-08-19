class Solution:
    def painters_partition(self,nums , k ,B):
        low = max(nums)
        high = sum(nums)
        while low <= high :
            mid = (low + high) // 2
            if self.can_paint(nums,k ,mid):
                ans  = mid 
                high = mid - 1
            else :
                low = mid + 1
        return (ans * B) %1000003             
    def can_paint(self , nums , k , mid ):
        total = 0
        painter  = 1
        for i in range(len(nums)):
            if total + nums[i] <= mid :
                total += nums[i]
            else :
                painter +=1 
                total = nums[i]
            if painter > k :
                return False
        return True            