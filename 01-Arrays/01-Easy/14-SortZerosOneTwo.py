# Brute force Approach to sort the 0 ,1 ,2
def SortZeroOneTwo(nums):
    count_0 = 0
    count_1 = 0
    count_2 = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count_0 +=1 
        elif nums[i] == 1:
            count_1 +=1
        else :
            count_2 +=1
    
    for i in range(count_0):
        nums[i] = 0
    for i in range(count_0 , count_0 + count_1):
        nums[i] = 1
    for i in range(count_0 + count_1,len(nums)):
        nums[i] = 2
    return nums

nums = [0, 2, 1, 2, 0, 1]
print(SortZeroOneTwo(nums))

# Time complexity : O(2n)
# -------------------------------------
# Optimal Solution :
class Solution:
    def sortZeroOneTwo(self, nums):
        low = 0
        mid = 0
        high = len(nums)-1
        while mid <= high :
            if nums[mid] == 0:
                nums[low] , nums[mid] = nums[mid] , nums[low]
                low+=1
                mid +=1
            elif nums[mid] == 1:
                mid +=1
            else :
                nums[mid] , nums[high] = nums[high] , nums[mid]
                high -=1
        return nums
# Time Complexity : O(n)

# -> The optimal solution was solved using the dutch nation flag .

# Intution  : 
# 0 to low-1 = 0 (the extreme left most) 
# low to mid - 1 contains 1 
# mid to high the unsorted part of the array 
# mid +1 to high  contains 2 the sorted half 

# Approach :
# low = 0 
# mid = 0
# high = len(nums)-1
# while low <= high :
#     if nums[mid] == 0:
#         swap nums[low] , nums[mid]
#         low+=1
#         mid +=1
#     elif nums[mid] == 1:
#         mid +=1
#     else :
#         swap nums[mid] nums[high]
#         high -=1


