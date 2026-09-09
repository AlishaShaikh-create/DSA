def Sort_array(nums):
    hashmap ={0:0,1:0,2:0}
    for i in range(len(nums)):
        hashmap[nums[i]]+=1
    j = 0
    for key , value in hashmap.items():
        while value :
            nums[j] = key
            j+=1
            value -=1
    return nums
nums = [1, 0, 2, 1, 0]

print(Sort_array(nums))     

# Using the Dutch nation flag
def Sort_array(nums):
    low = 0
    mid = 0
    high = len(nums)-1
    while mid <= high:
        if nums[mid] ==0:
            nums[mid] , nums[low] = nums[low] , nums[mid]
            low +=1
            mid +=1
        elif nums[mid] == 1:
            mid +=1
        else :
            nums[mid] , nums[high] = nums[high] , nums[mid]
            high -=1
    return nums                
nums = [1, 0, 2, 1, 0]
print(Sort_array(nums))     
