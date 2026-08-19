def Aggressive_cows(nums, k):
    nums.sort()
    def can_place(nums , k ,d):
        last_position = nums[0]
        count =  1 
        for i in range(1 , len(nums)):
            distance = nums[i] - last_position
            if distance >= d :
                count += 1
                last_position = nums[i]
            if count == k :
                return True
        return False
    
    ans = 0
    for d in range(1,(max(nums)-min(nums))+ 1):
        if can_place(nums, k, d):
            ans = d
    return ans

nums = [10, 1, 2, 7, 5]
k = 3

print(Aggressive_cows(nums, k))   

print("-------------------------------------")
# Optimal Solution
class Solution :
    def Aggressive_cows(self,nums,k):
        nums.sort()
        low = 0
        high = max(nums)- min(nums)
        ans = 0
        while low <= high :
            mid = (low + high)//2
            if self.can_place(nums , k ,mid):
                ans = mid 
                low = mid + 1
            else :
                high = mid - 1
        return ans            

    def can_place(self, nums , k , d):
        last_position = nums[0]
        count =  1
        for i in range(1 , len(nums)):
            distance = nums[i] - last_position
            if distance >= d:
                count +=1
                last_position = nums[i]
            if count == k :
                return True
        return False 
            

nums = [10, 1, 2, 7, 5]
k = 3

sol = Solution()
print(sol.Aggressive_cows(nums, k))