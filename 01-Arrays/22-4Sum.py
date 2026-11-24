class Solution:
    def fourSum(self, nums, target):
        i = 0
        nums.sort()
        result = []
        while i < len(nums)-3:
            if i > 0 and nums[i] == nums[i-1]:
                i+=1
                continue
            j = i+1
            while j < len(nums)-2:
                if j > i+1 and nums[j] == nums[j-1]:
                    j+=1
                    continue
                m = j+1
                n = len(nums)-1
                while m < n :
                    sum = nums[i] + nums[j] + nums[m] + nums[n]
                    if sum == target:
                        result.append([nums[i] , nums[j] , nums[m] , nums[n]])
                        m+=1
                        n-=1
                        while m < n and nums[m] == nums[m-1]:
                            m+=1    
                        while m < n and nums[n] == nums[n+1]:
                            n-=1
                    elif sum < target :
                        m+=1
                    else :
                        n-=1
                j+=1
            i+=1
        return result
                        
                    

                
        