class Solution:
    def majorityElement(self, nums):
        hashmap ={}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]]+=1
            else :
                hashmap[nums[i]] =1
        count = 0
        ele = 0
        for key , value in hashmap.items():
            if value > count :
                count =  value 
                ele = key
        return ele      

# using the moore voting algorithm :
def majority_element(nums):
    count = 0
    ele = 0
    for i in range(len(nums)):
        if count  == 0:
            ele = nums[i]
            count = 1
        elif  nums[i] == ele:
            count +=1
        else :
            count-=1
    return ele
nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
print(majority_element(nums))                