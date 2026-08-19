class Solution:
    def largestSubarraySumMinimized(self, a, k):
        low =  max(a)
        high = sum(a)
        ans = 0
        while low <= high:
            mid = (low + high)//2
            if self.can_sum(a,k,mid):
                ans = mid 
                high = mid -1
            else :
                low = mid + 1
        return ans            
    def can_sum(self , a , k , mid):
        total = 0
        count = 1
        for i in range(len(a)):
            if total + a[i] <= mid :
                total += a[i]
            else :
                count += 1
                total = a[i]
            if count > k:
                return False
        return True                    
        