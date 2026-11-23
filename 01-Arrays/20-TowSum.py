# Two Sum 

# Brute Force Approach 
def TwoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j]:
                return [i,j]
nums = [1, 6, 2, 10, 3]
target = 7
print(TwoSum(nums,target))

# time : O(n2) , space : O(1)

# Better:
def TwoSum(nums,target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i,hashmap[complement]]
        else :
            hashmap[nums[i]] = i
            
nums = [1, 6, 2, 10, 3]
target = 7
print(TwoSum(nums,target))

# time : O(n) , space : O(n)


# Optimal Solution :
def TwoSum(nums,target):
    nums.sort()