# Using the hashmap
# time - O(n) space - O(n)
def TwoSum(nums, target):
    hashmap ={}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        else :
            hashmap[nums[i]] = i

nums = [1, 6, 2, 10, 3]
target = 7            
print(TwoSum(nums, target))
nums = [1, 3, 5, -7, 6, -3]
target = 0
print(TwoSum(nums, target))

# using the two pointer in opposite direction
# time - O(N)+ O(NlogN) space - O(1)
