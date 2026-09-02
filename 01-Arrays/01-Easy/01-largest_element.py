class solution :
    def largest_element(self , nums):
        large = float('-inf')
        for i in range(len(nums)):
            if nums[i] > large:
                large = nums[i]
        return large

s  = solution()
nums = [3, 3, 6, 1]
print(s.largest_element(nums))            

            