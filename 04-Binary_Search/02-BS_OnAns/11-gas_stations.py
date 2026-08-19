import math
class Solution:
    def gas_station(self,nums,k):
        low = 0.0 
        high = 0
        for i in range(1,len(nums)):
            distance = nums[i]-nums[i-1]
            if distance > high :
                high = distance

        for _ in range(100):
            mid = (low + high)/2
            if self.can_place(nums,k,mid):
                high = mid 
            else :
                low = mid 
        return  high                  

            
    
    def can_place(self,nums,k,mid):
        station = 0
        for i in range(1, len(nums)):
            gap = nums[i] - nums[i-1]
            station += math.ceil(gap/mid)-1

            if station > k:
                return False
        return True    

arr = [0, 10]
k = 1
sol = Solution()
print(sol.gas_station(arr,k))        










