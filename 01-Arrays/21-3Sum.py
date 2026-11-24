# 3Sum 
def Three_sum(nums):
    nums.sort()
    i = 0
    result = []
    while i < len(nums)-2:
        if i > 0 and nums[i] == nums[i-1]:
            i+=1
            continue
        
        j = i+1
        k = len(nums)-1
        while j < k :
            sum = nums[i] + nums[j] + nums[k]
            if sum == 0:
                
                result.append([nums[i], nums[j],nums[k]])
                j+=1
                k-=1
                while j < k and nums[j] == nums[j-1]:
                    j+=1
                    
                while j < k and nums[k] == nums[k+1]:
                    k-=1
                    
            elif sum < 0:
                j+=1
            else:
                k-=1
        i+=1
    return result

nums = [2, -2, 0, 3, -3, 5]
print(Three_sum(nums))
nums = [2, -1, -1, 3, -1]
print(Three_sum(nums))
nums=[-3,0,0,3,3]
print(Three_sum(nums))
        