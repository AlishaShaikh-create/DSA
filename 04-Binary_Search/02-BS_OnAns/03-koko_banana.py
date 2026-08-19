import math
# Brute Force approach :
def koko_banana(nums , h):
    for i in range(1 , max(nums)+1):
        hours = 0
        for num in range(len(nums)):
            value = math.ceil(nums[num]/i)
            hours += value 
        if hours <= h :
            return i 
           
nums = [7, 15, 6, 3]
h = 8
print(koko_banana(nums,h))


print("--------------------------------")

def koko_banana(nums , h):
    low = 1 
    high = max(nums)
    while low <= high :
        mid = (low + high) // 2
        hours = 0
        for i in range(len(nums)):
            value = math.ceil(nums[i]/mid)
            hours += value
        if hours <= h :
            ans = mid 
            high = mid - 1
        else :
            low = mid + 1
    return ans                

nums = [7, 15, 6, 3]
h = 8
print(koko_banana(nums,h))            


nums = [25, 12, 8, 14, 19]
h = 5
print(koko_banana(nums,h))