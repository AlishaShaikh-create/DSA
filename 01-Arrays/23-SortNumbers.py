# Sort 0,1,2 in ascending order

# Brute Force Approach :Time : O(NlogN) Space: O(1)
# nums.sort()

# Better Solution : Time :O(2N) Space : O(1)
class Solution:
    def sortZeroOneTwo(self, nums):
        cnt0 = 0
        cnt1 = 0
        cnt2 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt0 +=1
            elif nums[i] == 1:
                cnt1 +=1
            else :
                cnt2 +=1
        for i in range(cnt0):
            nums[i] = 0
        for i in range(cnt0 , cnt0+cnt1):
            nums[i] = 1
        for i in range(cnt0+cnt1, len(nums)):
            nums[i] = 2
        return nums


# Optimal Solution :Time :O(N) Space : O(1)
# Intution :
#     -> 0 to low-1 : everything is sorted 0
#     -> low to mid -1 : everything is 1
#     -> mid to high-1:unsorted half
#     -> high to n : sorted with 2 
    
class Solution:
    def sortZeroOneTwo(self, nums):
        mid = 0
        low = 0
        high = len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                nums[low] , nums[mid] = nums[mid] , nums[low]
                low +=1
                mid +=1
            elif nums[mid] == 1:
                mid +=1
            else :
                nums[mid] , nums[high] = nums[high] , nums[mid]
                high -=1
        return nums