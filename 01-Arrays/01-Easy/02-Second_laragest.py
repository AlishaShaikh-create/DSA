class Solution :
    def second_largest(self , nums):
        largest = float('-inf')
        sec_largest = float('-inf')
        for i in range(len(nums)):
            if nums[i] > largest :
                sec_largest = largest
                largest = nums[i]
            elif nums[i] > sec_largest and nums[i]!= largest:
                sec_largest = nums[i]
        if sec_largest == float('-inf'):
            return -1
        else :
            return sec_largest

s = Solution()
nums = [8, 8, 7, 6, 5]
print(s.second_largest(nums))        

# time : O(n)
# space : O(1)