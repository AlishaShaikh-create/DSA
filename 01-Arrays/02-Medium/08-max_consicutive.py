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

