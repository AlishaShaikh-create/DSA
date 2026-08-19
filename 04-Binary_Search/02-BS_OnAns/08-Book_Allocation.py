class Solution :
    def findPages(self,nums,n):
        for p in range(max(nums),sum(nums)):
            if self.can_allocate(nums , n , p):
                return p 
            

    def can_allocate(self,nums,n,p):
        total = 0
        count = 1
        for i in range(len(nums)):
            if total + nums[i] <= p:
                total += nums[i]
            else :
                count += 1
                total = nums[i]
            if count > n:
                return False
        return True 
nums = [12, 34, 67, 90]
m=2
sol = Solution()
print(sol.findPages(nums,m))

print("-------------------------------------")
class Solution :
    def findPages(self,nums,n):
        ans = 0
        low = max(nums)
        high = sum(nums)
        while low <= high :
            mid = (low + high)//2
            if self.can_allocate(nums , n ,mid):
                ans = mid 
                high = mid - 1
            else :
                low = mid + 1
        return ans

         
            

    def can_allocate(self,nums,n,p):
        total = 0
        count = 1
        for i in range(len(nums)):
            if total + nums[i] <= p:
                total += nums[i]
            else :
                count += 1
                total = nums[i]
            if count > n:
                return False
        return True 

nums = [12, 34, 67, 90]
m=2
sol = Solution()
print(sol.findPages(nums,m))