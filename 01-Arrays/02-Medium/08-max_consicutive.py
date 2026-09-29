# Brute Force Approach

class Solution :
    def linear_search(self , nums, num):
        for i in range(len(nums)):
            if nums[i] == num:
                return True
        return False
    def longest_consecutive(self , nums):
        longest = 1
        if len(nums) <= 0:
            return 
        for i in range(len(nums)):
            ele = nums[i]
            count = 1
            while self.linear_search(nums , ele + 1):
                ele += 1
                count +=1
            longest = max(longest , count)
        return longest
nums  = [100, 4, 200, 1, 3, 2]
s = Solution()
print(s.longest_consecutive(nums))

# Time - O(n3)
# space - O(1)

# Move Zeroes :
print("Move zeroes to end")
def move_zeroes(nums):
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos] , nums[i] = nums[i] , nums[pos]
            pos +=1
    return pos 
nums = [0, 0, 0, 1, 3, -2]
print(move_zeroes(nums))